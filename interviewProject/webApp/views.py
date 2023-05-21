from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from datetime import datetime

from webApp.models import Cage, SensorData
from webApp.forms import CreateCageForm, UpdateCageForm


class CageListView(ListView):
    model = Cage
    template_name = 'index.html'
    context_object_name = 'cage'    
    paginate_by = 12
    ordering = '-id'


class CageCreateView(CreateView):

    model = Cage
    template_name = 'add-cage.html'
    form_class = CreateCageForm

    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        form = CreateCageForm(request.POST)

        if form.is_valid():
            label = form.cleaned_data['label']
            Cage.objects.create(label=label)
        else:
            messages.error(request, f'Creating new cage was was failed')
            return render(request, 'add-cage.html', {'form': CreateCageForm()})
        
        messages.success(request, f'Cage {label} created successfully')
        return redirect ("cage-list")

    def get(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        return super().get(request, *args, **kwargs)
    

class CageDetailView(DetailView):
    model = Cage
    template_name = "cage-detail.html"
    context_object_name = 'cage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cage = self.get_object()
        today = datetime.today()
        today_sensor_data = cage.sensor_data_rows.filter(timestamp__date=today)
        context = {
            'cage': cage,
            'today_sensor_data': today_sensor_data,
            'today_health_data': cage.sensor_data_rows.filter(timestamp__date=today, is_successful=True)
        }
        return context
    

class UpdateCageView(UpdateView):

    model = Cage
    template_name = 'edit-cage.html'
    form_class = UpdateCageForm

    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        form = CreateCageForm(request.POST)
        cage_pk = self.kwargs['pk']
        cage = Cage.objects.get(pk=cage_pk)

        if form.is_valid():
            label = form.cleaned_data['label']
            Cage.objects.filter(pk=cage_pk).update(label=label)
        else:
            messages.error(request, f'Try again!')
            return render(request, 'edit-cage.html', {'form': form, 'object': cage})
        
        messages.success(request, f'Cage edited successfully')
        return redirect ("cage-list")

    def get(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        return super().get(request, *args, **kwargs)
    

class DeleteCageView(DeleteView):
    model = Cage
    template_name = 'delete-cage.html'

    def get_success_url(self):
        self.cage = self.get_object()
        messages.success(self.request, f"Cage {self.cage.label} deleted successfuly.")  
        url = reverse('cage-list')
        return url
