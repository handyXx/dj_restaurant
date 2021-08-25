from django.shortcuts import render
from .models import Category, Meal, Reviewer

from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

class AllMealsView(ListView):
    queryset = Meal.objects.all()
    template_name = 'meals/index.html'
    context_object_name = "meals"
    
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        category = Category.objects.all().distinct()
        reviewer = Reviewer.objects.all()
        context['categories'] = category
        context['first_reviewer'] = reviewer[0]
        context['reviewers'] = reviewer[1:]
        return context

class MealDetailsView(DetailView):
    model = Meal
    template_name = 'meals/meal_detail.html'
    context_object_name = "meal"


