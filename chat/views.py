from django.shortcuts import render, get_object_or_404
from .models import User, Room , Message
# Create your views here.
def home_view(request):
    room = Room.objects.all()
    context = {
        "rooms": room
    }
    return render(request, 'chat/home.html', context)         

def room_view(request,id=None):
    # Fetch the room using the room_id from the URL
    room = get_object_or_404(Room, id=id)
    
    # Fetch all messages for the room
    messages = Message.objects.filter(room=room).order_by('sent_at')
    
    # Pass the room and messages to the context
    context = {
        'room': room,
        'messages': messages
    }
    
    # Render the template with the context
    return render(request, 'chat/room.html', context)
    