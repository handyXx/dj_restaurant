from django.contrib import admin
from .models import Stuff

@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    pass
