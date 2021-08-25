from django.db import models
from django.db.models.fields.files import ImageField

class Stuff(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=70)
    image=  ImageField(upload_to='stuff/')
    facebook_url = models.URLField(max_length=250)
    twitter_url = models.URLField(max_length=250)
    instagram_url = models.URLField(max_length=250)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Stuff"

