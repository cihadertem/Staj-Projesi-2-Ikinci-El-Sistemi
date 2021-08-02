from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Room,Message
from users.models import CustomUser

def index(request):
    if not request.user.is_authenticated:
        raise Http404()
    users=CustomUser.objects.all().exclude(username=request.user)

    return render(request, 'chat/index.html',{"users":users})

def room(request, room_name):
    if not request.user.is_authenticated:
        raise Http404()
    users = CustomUser.objects.all().exclude(username=request.user)
    room=Room.objects.get(id=room_name)
    messages=Message.objects.filter(room=room)

    return render(request, 'chat/room_v2.html', {'room_name': room_name,"room":room,"users":users,"messages":messages})


def start_chat(request, username):
    if not request.user.is_authenticated:
        raise Http404()
    second_user=CustomUser.objects.get(username=username)
    try:
        room=Room.objects.get(first_user=request.user,second_user=second_user)


    except Room.DoesNotExist:
        try:
            room = Room.objects.get(second_user=request.user, first_user=second_user)
        except Room.DoesNotExist:
            room=Room.objects.create(first_user=request.user,second_user=second_user)
    return redirect("chats:room",room.id)
# Create your views here.
