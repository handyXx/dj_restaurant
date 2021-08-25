from django.db import models
from django.utils.text import slugify

class Meal(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True)
    preperation_time = models.IntegerField()
    image = models.ImageField(upload_to="meals/")
    slug = models.SlugField(null=True, blank=True)
    

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ["name"]

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Reviewer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    review = models.TextField()
    image = models.ImageField(upload_to='reviewers/')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
