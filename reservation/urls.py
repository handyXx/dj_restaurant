from django.urls import path
from .views import ReservationView

app_name = 'reservation'

urlpatterns = [
    path('', ReservationView.as_view(), name="reservation"),
]