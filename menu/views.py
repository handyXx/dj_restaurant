from django.shortcuts import render
from meals.models import Meal, Category, Reviewer
from django.views.generic import (
    ListView
)

class MenuPageView(ListView):
    queryset = Meal.objects.all()
    template_name = 'menu/menu.html'
    context_object_name = "meals"

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        category = Category.objects.all().distinct()
        reviewer = Reviewer.objects.all()
        context['categories'] = category
        context['first_reviewer'] = reviewer[0]
        context['reviewers'] = reviewer[1:]
        return context