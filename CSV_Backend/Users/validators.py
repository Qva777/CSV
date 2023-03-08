import re
from django.core.exceptions import ValidationError


def validate_password(password):
    """ Validator password """
    if len(password) < 8:
        raise ValidationError('Password must be at least 8 characters long.')
    if not re.search('[A-Z]', password):
        raise ValidationError('Password must contain at least one uppercase letter.')
    if not re.search('[0-9]', password):
        raise ValidationError('Password must contain at least one number.')
