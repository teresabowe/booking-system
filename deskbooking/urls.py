from . import views
from django.urls import path


urlpatterns = [
    path('', views.view_home, name='home'),
    path("view_bookings/", views.BookingsList.as_view(), name="view_bookings"),
    path('add_booking/', views.AddBookingView.as_view(), name="add_booking"),
    path('load_desks/', views.load_desks, name='ajax_load_desks'),
    path('<int:pk>/delete_booking/', views.DeleteBooking.as_view(),
         name="delete_booking"),
    path('<int:pk>/update_booking/', views.UpdateBooking.as_view(),
         name="update_booking"),
]
