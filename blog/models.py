from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager
from meals.models import Category

class Post(models.Model):
    title = models.CharField(max_length=150)
    hook = models.CharField(max_length=350)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    slug = models.SlugField(null=True, blank=True, max_length=150)
    date_published = models.DateField(auto_now=True)
    time_published = models.TimeField(auto_now=True)
    bg_cover = models.ImageField(upload_to="blog-posts-bg/", default=None)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL , null=True)
    tags = TaggableManager(blank=True)


    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            if not len(self.slug) < 150:
                self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_published']

class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.content)
    
    class Meta:
        ordering = ['-created']
