from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Service

@admin.register(Service)
class ServiceAdmin(TranslatableAdmin):
    list_display = ['name']
