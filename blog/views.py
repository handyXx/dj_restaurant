from blog.models import Post, Comment
from django.views.generic import (
    ListView,
    DetailView
)
from django.views.generic.edit import FormMixin
from .models import Post
from .forms import CommentForm
from django.urls import reverse
from taggit.models import Tag
from meals.models import Category
from django.db.models import Q

class BlogView(ListView):
    queryset = Post.objects.all()
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    success_url = '/blog/'

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        queryset = Post.objects.all()
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains = search_query)|
                Q(content__icontains= search_query) |
                Q(category__name__icontains=search_query) |
                Q(tags__name__icontains= search_query)
        ).distinct()

        return queryset

class PostDetailView(FormMixin, DetailView):
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    form_class = CommentForm
    
    def get_queryset(self):
        query_set = Post.objects.filter(slug=self.kwargs['slug'])
        try:
            if query_set:
                query_set.content = [strng for strng in f"""{query_set.content}""".split('\n') if strng != '']
            return query_set
        
        except AttributeError:
            return query_set

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        post = Post.objects.filter(slug=self.kwargs['slug'])
        # context args
        context['comments_list'] = Comment.objects.filter(post__in=post)
        context["form"] = self.get_form()
        context['tags'] = Tag.objects.all()
        context['categroies'] = Category.objects.all()
        if len(Post.objects.all()) < 4:
            context['recent_posts'] = Post.objects.all()
        else:
            context['recent_posts'] = Post.objects.all()[:3]
        
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = self.object
            new_comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.slug})
    

class TagPostView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__name__in=[self.kwargs['tag']])

class CategoryPostView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        ctg = Category.objects.get(name=self.kwargs['category'])
        return Post.objects.filter(category=ctg)
    