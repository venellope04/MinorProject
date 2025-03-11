from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder  # Assuming you're using this for token generation
import time
import random

# Home Page View
def home(request):
    return render(request, 'conferencing/home.html')

# Video Call Room View
def video_call(request, room_name):
    return render(request, 'conferencing/room.html', {'room_name': room_name})

# Agora Token Generation View
def get_agora_token(request):
    app_id = '71fbf1e2263a49869725faa8404523ec'
    app_certificate = 'c30096eedb10445fb0990cb0d0a4f15b' 
    channel_name = request.GET.get('channelName')
    uid = random.randint(1, 230)  # Unique ID for each user
    role = 1  # 1 for publisher
    expire_time = 3600  # Token expiry in seconds

    current_time = int(time.time())
    privilege_expired_ts = current_time + expire_time

    token = RtcTokenBuilder.buildTokenWithUid(app_id, app_certificate, channel_name, uid, role, privilege_expired_ts)

    return JsonResponse({'token': token, 'uid': uid})
