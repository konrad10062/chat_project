# chat/views.py
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


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
