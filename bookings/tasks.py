from celery import shared_task
from .models import Booking

@shared_task
def send_booking_confirmation(booking_id):
    booking = Booking.objects.get(id=booking_id)
    print(f"Booking confirmed for {booking.user.email} for event {booking.event.title}")
