from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, TemplateView, DeleteView
from django.contrib.auth.views import LoginView
from autopark.models import Vehicle, Booking, Location
from autopark.forms import VehicleForm, BookingForm
from rest_framework import viewsets
from autopark.models import Vehicle
from autopark.serializers import VehicleSerializer, LocationSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from autopark.filters import VehicleFilter
from rest_framework import filters
from django.urls import reverse_lazy

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

class VehicleViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = VehicleFilter
    ordering_fields = ['number', 'vehicle_type', 'created_at']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class LocationListView(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)