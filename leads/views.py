from django.shortcuts import render,redirect
from .models import Lead
from .forms import LeadModelForm

def lead_list(request):
    context = {'leads': Lead.objects.all()}
    return render(request, 'lead_list.html', context)

def lead_detail(request, pk):
    context = {'lead': Lead.objects.get(id=pk)}
    return render(request, 'lead_detail.html', context)

def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {'form': form}
    return render(request, 'lead_create.html', context)

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {'form': form, 'lead': lead}
    return render(request, 'lead_update.html', context)