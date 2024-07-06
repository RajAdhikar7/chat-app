from django.shortcuts import render, get_object_or_404 , redirect
from .models import User, Room , Message
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import login

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a success page
    else:
        form = CustomUserCreationForm()
    return render(request, 'chat/register.html', {'form': form})

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

