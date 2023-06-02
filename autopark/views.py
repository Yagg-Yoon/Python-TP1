from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, TemplateView, DeleteView
from django.contrib.auth.views import LoginView
from autopark.models import Vehicle, Booking
from autopark.forms import VehicleForm, BookingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import datetime

class AllListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'all_table.html'
    context_object_name = 'table_data'

class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'vehicle_details.html'
    context_object_name = 'vehicle'

class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'create_form.html'
    success_url = 'all'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

class LoginFormView(LoginView):
    template_name = 'registration/login.html'

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'registration/delete_account.html'
    success_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        return self.request.user

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_change_done')

class CustomPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_all')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'
    ordering = ['booking_from']

class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'booking_delete.html'
    success_url = reverse_lazy('booking_all')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)