# chat/views.py
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login
def home(request):
    return render(request, 'home.html')



def index(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RoomForm()

    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms, 'form': form})


def room(request, room_name):
    room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'chat/room.html', {'room_name': room_name})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'chat/login.html', {'error': 'Invalid credentials'})
    return render(request, 'chat/login.html')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})