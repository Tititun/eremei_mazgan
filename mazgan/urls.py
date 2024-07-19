from django.urls import path
from . import views

app_name = 'mazgan'

urlpatterns = [
    path('', views.main_page, name='main')
]