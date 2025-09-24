from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Event, Booking
from django.contrib import messages

# Home page - list all events
def index(request):
    events = Event.objects.all()
    return render(request, 'bookings/index.html', {'events': events})

# Register new user
from .forms import CustomUserCreationForm  # import the custom form

from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from users.forms import CustomUserCreationForm  # ✅ import custom form

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after register
            messages.success(request, "Account created successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'bookings/register.html', {'form': form})

# Book an event
@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        Booking.objects.create(user=request.user, event=event)
        return redirect('my_bookings')
    return render(request, 'bookings/book_event.html', {'event': event})
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('home')  # Redirect to home after login
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "bookings/login.html")

    return render(request, "bookings/login.html")


# View my bookings
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})
