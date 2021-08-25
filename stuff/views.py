from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import Stuff
from meals.models import Meal
from meals.models import Reviewer

class StuffView(ListView):
    model = Stuff
    template_name = "stuff/stuff.html"
    context_object_name = "stuff"

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        reviewer = Reviewer.objects.all()
        context['first_reviewer'] = reviewer[0]
        context['reviewers'] = reviewer[1:]
        return context
