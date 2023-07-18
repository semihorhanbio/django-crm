from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

def home_page(request):
    context = {'leads': Lead.objects.all()}
    return render(request, 'home.html', context)