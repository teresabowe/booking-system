from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Booking


def view_home(request):
    """
    View Home Page
    """
    return render(request, 'index.html')


class BookingsList(LoginRequiredMixin, generic.ListView):
    """
    View Bookings
    """
    login_url = '../accounts/login/'
    redirect_field_name = 'account_login'
    model = Booking
    queryset = Booking.objects.all()
    template_name = "view_bookings.html"

    def get_queryset(self):
        return super().get_queryset().filter(desk_user=self.request.user).\
         order_by('desk_booking_date')
