from django.shortcuts import render
from django.views.generic import ListView

from webApp.models import Cage


class CageListView(ListView):
    model = Cage
    template_name = 'index.html'
