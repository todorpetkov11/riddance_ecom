from django.core.exceptions import ValidationError
import os


def image_validator(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpeg', '.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
