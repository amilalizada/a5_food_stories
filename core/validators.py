from django.core.exceptions import ValidationError

def validate_email(value):
    """
    Validate the email value.

    Parameters:
        value (str): The email value to be validated.

    Raises:
        ValidationError: If the email value does not contain 'amil'.

    Returns:
        None
    """
    if 'com' not in value:
        raise ValidationError('Email must contain com')