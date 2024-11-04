from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    tag = models.ForeignKey('Tag', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE) 

    objects = models.Manager()

    def __str__(self):
        return str(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=60)
    objects = models.Manager()

    def __str__(self):
        return str(self.title)
