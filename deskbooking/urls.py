from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_home, name='home'),
    path("view_bookings/", views.BookingsList.as_view(), name="view_bookings"),
    path('add_booking/', views.AddBookingView.as_view(), name="add_booking"),
    path('load_desks/', views.load_desks, name='ajax_load_desks'),
]
