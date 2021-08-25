from django.contrib import admin
from .models import Meal, Category, Reviewer

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Reviewer)
class ReviewerAdmin(admin.ModelAdmin):
    pass
