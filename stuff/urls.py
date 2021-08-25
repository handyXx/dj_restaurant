from django.urls import path
from .views import StuffView

app_name  = 'stuff'

urlpatterns = [
    path('', StuffView.as_view(), name='stuff_list'),
]