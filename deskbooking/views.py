from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from . forms import AddForm
from django.views import generic
from .models import Booking, Desk


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


class AddBookingView(LoginRequiredMixin, CreateView):
    """
    Add Bookings
    """
    login_url = '../accounts/login/'
    redirect_field_name = 'account_login'
    model = Booking
    form_class = AddForm
    template_name = 'add_booking.html'
    success_url = '/view_bookings/'

    def get_initial(self):
        return {'desk_user': self.request.user}

    def form_valid(self, form):
        form.instance.sequence = Booking.objects.filter(desk_user=self.request.user)
        return super().form_valid(form)


class DeleteBooking(LoginRequiredMixin, DeleteView):
    """
    Delete Bookings
    """
    login_url = '../accounts/login/'
    redirect_field_name = 'account_login'
    model = Booking
    template_name = "booking_confirm_delete.html"
    success_url = '/view_bookings/'


@login_required()
def load_desks(request):
    """
    Create queryset for add booking dropdown
    """
    desk_booking_date_field = request.GET.get('desk_booking_date')
    bookings = Booking.objects.values_list('desk', flat=True).filter(desk_booking_date=desk_booking_date_field)
    desks = Desk.objects.values_list('id', flat=True)
    pk_list = desks.difference(bookings)
    queryset = Desk.objects.filter(pk__in=pk_list)

    return render(request, 'desk_dropdown_list_options.html', {'mydesks': queryset})
