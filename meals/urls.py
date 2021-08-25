from django.urls import path
from .views import (
    AllMealsView,
    MealDetailsView
)

app_name = "meals"

urlpatterns = [
    path('', AllMealsView.as_view(), name="meals_list"),
    path('<slug:slug>', MealDetailsView.as_view(), name="meal_detail"),

]