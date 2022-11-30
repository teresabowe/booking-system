from django import forms
from .models import Booking


class AddForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('desk_user', 'desk_booking_date', 'desk')
        widgets = {
            'desk_booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 'desk_user': forms.HiddenInput,
        }


class BookingUpdateForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('desk_booking_date', 'desk')
        widgets = {
            'desk_booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 'desk_user': forms.HiddenInput,
        }
