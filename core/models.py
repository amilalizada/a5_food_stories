from django.db import models
from core.validators import validate_email

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(validators=[validate_email])
    subject = models.CharField(max_length=30)
    message = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
