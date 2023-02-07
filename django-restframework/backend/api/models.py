from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=300, null=True)
    body = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title
