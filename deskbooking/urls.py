from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_home, name='home'),
    path("view_bookings/", views.BookingsList.as_view(), name="view_bookings"),
]
