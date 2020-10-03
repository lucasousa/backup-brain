from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse


class Wiki(models.Model):
    title = models.CharField(max_length=255)
    description = HTMLField()
    created_at = models.DateTimeField('Data de publicação', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('wiki:create_wiki')

    def __str__(self):
        return self.title