from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Photo, PhotoGroup, Service

@admin.register(Service)
class ServiceAdmin(TranslatableAdmin):
    list_display = ['name']

class PhotoInline(admin.TabularInline):
    model = Photo

@admin.register(PhotoGroup)
class PhotoGroupAdmin(TranslatableAdmin):
    inlines = [PhotoInline]
