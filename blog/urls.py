from django.urls import path
from .views import BlogView, PostDetailView, TagPostView, CategoryPostView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='main_blog'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('tags=<slug:tag>' , TagPostView.as_view() , name='post_by_tag'),
    path('category=<slug:category>' , CategoryPostView.as_view() , name='post_by_category'),
]