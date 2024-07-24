from django.urls import path
from . import views

app_name = 'mazgan'

urlpatterns = [
    path('price_list', views.price_list, name='price_list'),
    path('', views.main_page, name='main')
]