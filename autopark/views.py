from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from autopark.models import Vehicle
from autopark.forms import VehicleForm

class AllListView(ListView):
    model = Vehicle
    template_name = 'all_table.html'
    context_object_name = 'table_data'

class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_details.html'
    context_object_name = 'vehicle'

class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'create_form.html'
    success_url = 'all'