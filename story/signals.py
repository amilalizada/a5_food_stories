from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from slugify import slugify
from story.models import Recipe


@receiver(post_save, sender=Recipe)
def post_save(sender, created, **kwargs):
    if created:
        instance = kwargs["instance"]
        instance.slug = slugify(instance.title, replacements=[['n', 'm']])
        instance.slug = instance.slug + '-' + str(datetime.now().timestamp()).replace('.', '')
        instance.save()
    
    