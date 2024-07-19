from django.http import HttpRequest
from django.shortcuts import render

def main_page(request: HttpRequest):
    return render(request, 'mazgan/base.html')
