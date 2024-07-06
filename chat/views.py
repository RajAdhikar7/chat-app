from django.shortcuts import render, get_object_or_404
from .models import User, Room , Message
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_view(request):
    room = Room.objects.all()
    context = {
        "rooms": room
    }
    return render(request, 'chat/home.html', context)

@login_required
def room_view(request, id=None):
    room = get_object_or_404(Room, id=id)
    messages = Message.objects.filter(room=room).order_by('sent_at')
    context = {
        'room': room,
        'messages': messages
    }
    return render(request, 'chat/room.html', context)