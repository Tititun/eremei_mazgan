from django.http import HttpRequest
from django.shortcuts import render
from .forms import BidForm
from .models import Service

def main_page(request: HttpRequest):
    if request.method == 'GET':
        form = BidForm()
    return render(request, 'mazgan/main.html',
                  {'current_page': 'home',
                   'form': form})


def price_list(request: HttpRequest):
    language = request.LANGUAGE_CODE
    services = Service.objects.filter(translations__language_code=language)
    return render(request, 'mazgan/price_list.html',
                  {'services': services, 'current_page': 'price_list'})
