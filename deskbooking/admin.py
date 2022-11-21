from django.contrib import admin
from .models import Desk
from .models import Booking


@admin.register(Desk)
class DeskAdmin(admin.ModelAdmin):
    list_display = ('desk', 'floor', 'description', 'created_on')
    list_filter = ('floor', 'created_on')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('desk', 'desk_user', 'desk_booking_date', 'created_on')
    list_filter = ('desk_user', 'created_on')
