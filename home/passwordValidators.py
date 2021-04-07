import re  # Regular expression
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class NumberValidator(object):
    def __init__(self, nb=2):
        self.nb = nb

    def validate(self, password, user=None):
        if not re.findall('[0-9]{' + str(self.nb) + ',}', password):
            raise ValidationError(
                _("Votre mot de passe doit contenir au moins %(nb)d chiffre(s)."),
                code='password_no_number',
                params={'nb': self.nb},
            )

    def get_help_text(self):
        return _(
            "Votre mot de passe doit contenir au moins %(nb)d chiffre(s)."
            % {'nb': self.nb}
        )


class UppercaseValidator(object):
    def __init__(self, nb=1):
        self.nb = nb

    def validate(self, password, user=None):
        if not re.findall('[A-Z]{' + str(self.nb) + ',}', password):
            raise ValidationError(
                _("Votre mot de passe doit contenir au moins %(nb)d lettre(s) majuscule(s)."),
                code='password_no_upper',
                params={'nb': self.nb},
            )

    def get_help_text(self):
        return _(
            "Votre mot de passe doit contenir au moins %(nb)d lettre(s) majuscule(s)."
            % {'nb': self.nb}
        )


class LowercaseValidator(object):
    def __init__(self, nb=2):
        self.nb = nb

    def validate(self, password, user=None):
        if not re.findall('[a-z]{' + str(self.nb) + ',}', password):
            raise ValidationError(
                _("Votre mot de passe doit contenir au moins %(nb)d lettre(s) minuscule(s)."),
                code='password_no_lower',
                params={'nb': self.nb},
            )

    def get_help_text(self):
        return _(
            "Votre mot de passe doit contenir au moins %(nb)d lettre(s) minuscule(s)."
            % {'nb': self.nb}
        )


class SymbolValidator(object):
    def __init__(self, nb=2):
        self.nb = nb

    def validate(self, password, user=None):
        if not re.findall('[\(\/)\[\]\{\}\|`~!@#\$%\^&\*_\-+=;:\'",<>./?]{' + str(self.nb) + ',}', password):
            raise ValidationError(
                _("Votre mot de passe doit contenir au moins %(nb)d caractère(s) spécial(aux)"),
                code='password_no_symbol',
                params={'nb': self.nb},
            )

    def get_help_text(self):
        return _(
            "Votre mot de passe doit contenir au moins %(nb)d caractère(s) spécial(aux)"
            % {'nb': self.nb}
        )
