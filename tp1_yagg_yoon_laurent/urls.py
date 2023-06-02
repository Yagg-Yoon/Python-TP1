"""
URL configuration for tp1_yagg_yoon_laurent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from autopark.views import AllListView, VehicleDetailView, VehicleCreateView, LoginFormView, DashboardView, BookingCreateView
from autopark.views import UserCreateView, UserDeleteView, CustomPasswordChangeView, CustomPasswordChangeDoneView
from autopark.views import BookingListView, BookingDeleteView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("autopark/all", AllListView.as_view(), name='all_vehicles'),
    path("autopark/<int:pk>/details", VehicleDetailView.as_view(), name="vehicle_details"),
    path("autopark/create", VehicleCreateView.as_view(), name="add_vehicle"),
    path("", DashboardView.as_view()),
    path("accounts/login", LoginFormView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/delete/', UserDeleteView.as_view(), name='delete_account'),
    path('accounts/password/change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password/change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('booking/new', BookingCreateView.as_view(), name='booking_new'),
    path('booking/all', BookingListView.as_view(), name='booking_all'),
    path('booking/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete')
]
