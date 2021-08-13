from django.core.exceptions import ValidationError


def phone_validator(value):
    if not value.startswith('0'):
        raise ValidationError('Invalid phone number!')


def full_name_validator(value):
    if len(value.split(' ')) < 2:
        raise ValidationError('Please enter a first name and a surname!')
    if not value.isalpha():
        raise ValidationError('Please enter valid names!')
    if not value.istitle():
        raise ValidationError('All names must be capitalized!')

