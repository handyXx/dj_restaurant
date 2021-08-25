from django.views.generic import ListView
from meals.models import Meal
from meals.models import Reviewer

class GalleryView(ListView):
    model = Meal
    template_name = "gallery/gallery.html"
    context_object_name = "meals"
    
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        reviewer = Reviewer.objects.all()
        context['first_reviewer'] = reviewer[0]
        context['reviewers'] = reviewer[1:]
        return context

