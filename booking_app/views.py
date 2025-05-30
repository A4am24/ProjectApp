from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Hotel
from django.contrib import messages
from django.shortcuts import render, redirect

print('Adam')
# Create your views here.

def index(request):
    return render(request, 'index.html')

def hotel_view(request):
    hotels = Hotel.objects.all()
    context = {'hotels': hotels}
    return render(request, 'hotel_view.html', context)

def booking(request):
    hotels = Hotel.objects.all()
    return render(request, 'booking.html', {'hotels': hotels})

def create_login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("I'm valid")
            user = form.save()
            login(request, user)
            messages.success(request, 'Account successfully created.')
            print("redirecting")
            return redirect('enter_login.html')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()

    return render(request, 'create_login.html', {'form': form})


def enter_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index.html')
    else:
        form = AuthenticationForm()
    return render(request, 'enter_login.html', {'form': form})


