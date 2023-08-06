"""Forms related to aliases management."""

from collections import OrderedDict

from django import forms
from django.http import QueryDict
from django.utils.translation import ugettext as _, ugettext_lazy

from modoboa.lib.email_utils import split_mailbox
from modoboa.lib.exceptions import BadRequest, NotFound, Conflict
from modoboa.lib.form_utils import (
    DynamicForm
)

from ..models import Domain, Mailbox, Alias
from .. import signals


class AliasForm(forms.ModelForm, DynamicForm):

    """A form to create/modify an alias."""

    email = forms.EmailField(
        label=ugettext_lazy("Email address"),
        help_text=ugettext_lazy(
            "The distribution list address. Use the '*' character to create a "
            "'catchall' address (ex: *@domain.tld)."
        ),
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    recipients = forms.EmailField(
        label=ugettext_lazy("Recipients"), required=False,
        help_text=ugettext_lazy(
            "Mailbox(es) this alias will point to. Indicate only one address "
            "per input, press ENTER to add a new input."
        ),
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Alias
        fields = ("enabled",)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AliasForm, self).__init__(*args, **kwargs)
        self.fields = OrderedDict(
            (key, self.fields[key]) for key in
            ['email', 'recipients', 'enabled']
        )

        if len(args) and isinstance(args[0], QueryDict):
            if "instance" in kwargs:
                if not kwargs["instance"].domain.enabled:
                    del self.fields["enabled"]
            self._load_from_qdict(args[0], "recipients", forms.EmailField)
        elif "instance" in kwargs:
            dlist = kwargs["instance"]
            self.fields["email"].initial = dlist.full_address
            if not dlist.domain.enabled:
                self.fields["enabled"].widget.attrs["disabled"] = "disabled"
            cpt = 1
            for al in dlist.aliases.all():
                name = "recipients_%d" % cpt
                self._create_field(forms.EmailField, name, al.full_address, 2)
                cpt += 1
            for mb in dlist.mboxes.all():
                name = "recipients_%d" % (cpt)
                self._create_field(forms.EmailField, name, mb.full_address, 2)
                cpt += 1
            for addr in dlist.extmboxes.split(','):
                if addr == "":
                    continue
                name = "recipients_%d" % (cpt)
                self._create_field(forms.EmailField, name, addr, 2)
                cpt += 1

    def clean_email(self):
        localpart, domname = split_mailbox(self.cleaned_data["email"])
        try:
            domain = Domain.objects.get(name=domname)
        except Domain.DoesNotExist:
            raise forms.ValidationError(_("Domain does not exist"))
        if not self.user.can_access(domain):
            raise forms.ValidationError(
                _("You don't have access to this domain")
            )
        return self.cleaned_data["email"].lower()

    def set_recipients(self):
        """Recipients dispatching

        We make a difference between 'local' recipients (the ones hosted
        by Modoboa) and 'external' recipients.
        """
        self.ext_rcpts = []
        self.int_rcpts = []
        total = 0

        for k, v in self.cleaned_data.items():
            if not k.startswith("recipients"):
                continue
            if v == "":
                continue
            local_part, domname, extension = (
                split_mailbox(v, return_extension=True))
            if domname is None:
                raise BadRequest(
                    u"%s %s" % (_("Invalid mailbox"), v)
                )
            domain = Domain.objects.filter(name=domname).first()

            if (
                (domain is not None) and
                (
                    any(
                        r[1] for r in signals.use_external_recipients.send(
                            self, recipients=v)
                    ) is False
                )
            ):
                rcpt = Alias.objects.filter(
                    domain=domain, address=local_part).first()
                if rcpt and (rcpt.full_address == self.cleaned_data["email"]):
                    rcpt = None
                if rcpt is None:
                    try:
                        rcpt = Mailbox.objects.get(
                            domain=domain, address=local_part)
                    except Mailbox.DoesNotExist:
                        raise NotFound(
                            _("Local recipient {}@{} not found")
                            .format(local_part, domname)
                        )
                if extension is None:
                    if rcpt in self.int_rcpts:
                        raise Conflict(
                            _("Recipient {} already present").format(v)
                        )
                    self.int_rcpts += [rcpt]
                    total += 1
                    continue

            if v in self.ext_rcpts:
                raise Conflict(
                    _("Recipient %s already present" % v)
                )
            self.ext_rcpts += [v]
            total += 1

        if total == 0:
            raise BadRequest(_("No recipient defined"))

    def save(self, commit=True):
        """Custom save method."""
        alias = super(AliasForm, self).save(commit=False)
        local_part, domname = split_mailbox(self.cleaned_data["email"])
        alias.address = local_part
        alias.domain = Domain.objects.get(name=domname)
        if commit:
            alias.save(int_rcpts=self.int_rcpts, ext_rcpts=self.ext_rcpts)
            self.save_m2m()
        return alias
