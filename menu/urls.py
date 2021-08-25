from django.urls import path
from .views import MenuPageView

app_name = 'menu'

urlpatterns = [
    path('', MenuPageView.as_view(), name='menu'),
]