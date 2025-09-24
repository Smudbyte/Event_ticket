from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Event, Booking

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date', 'total_seats', 'available_seats')
    search_fields = ('title', 'location')
    list_filter = ('date',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'seats_booked', 'status', 'created_at')
    list_filter = ('status', 'event')
    search_fields = ('user__username', 'event__title')
