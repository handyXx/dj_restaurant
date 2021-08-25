from django.contrib import admin
from .models import Post, Comment
from taggit.models import Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
