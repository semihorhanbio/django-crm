from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

def lead_list(request):
    context = {'leads': Lead.objects.all()}
    return render(request, 'lead_list.html', context)

def lead_detail(request, pk):
    context = {'lead': Lead.objects.get(id=pk)}
    return render(request, 'lead_detail.html', context)