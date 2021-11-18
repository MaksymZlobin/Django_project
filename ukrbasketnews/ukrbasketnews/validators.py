from django.core.exceptions import ValidationError
from django.utils.translation import ngettext


class CustomMinimumLengthValidator:
    """
    Custom password validation against faggiest password
    """

    def __init__(self, min_length=4):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "This password is for fags. It must contain at least %(min_length)d character.",
                    "This password is for fags. It must contain at least %(min_length)d characters.",
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return ngettext(
            "Your password must contain at least %(min_length)d character, if you don't want to be fag",
            "Your password must contain at least %(min_length)d characters, if you don't want to be fag",
            self.min_length
        ) % {'min_length': self.min_length}
