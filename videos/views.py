from django.shortcuts import render
from .models import Song,Audio
from django.views.decorators.csrf import csrf_exempt
import os
from pathlib import Path
from django.core.files.storage import FileSystemStorage
import ffmpeg_streaming
from ffmpeg_streaming import Formats
from django.http import HttpResponse


BASE_DIR = Path(__file__).resolve().parent.parent

def home(request):
    context={
        'songs':Song.objects.all()
    }
    return render(request,'videos/list.html',context)

@csrf_exempt
def upload(request):
    if request.method=="POST":
        uploaded_file = request.FILES['myFile']
        name_array=uploaded_file.name.split('.')
        uploaded_file.name=name_array[0]
        song=Song.objects.create(title=request.POST.get('title'),description=request.POST.get('description'),artist=request.POST.get('artist'),path=f'{uploaded_file.name}')
        song.save()
        song=Song.objects.all().last()
        id=song.id
        os.mkdir(f'{BASE_DIR}\\media\\{id}\\')
        fs=FileSystemStorage(BASE_DIR)
        fs.save(uploaded_file.name,uploaded_file)
        video = ffmpeg_streaming.input(f'{BASE_DIR}\\{uploaded_file.name}')
        dash = video.dash(Formats.h264())
        dash.auto_generate_representations()
        dash.output(f'{BASE_DIR}\\media\\{id}\\{uploaded_file.name}.mpd')
        os.remove(f'{BASE_DIR}\\{uploaded_file.name}')
        return HttpResponse("uploaded successfully")
    return render(request,'videos/upload.html')

def player(request,id):
    context={
        'song':Song.objects.get(id=id),
        
    }
    return render(request,'videos/watch.html',context)

def audio_player(request):
    context={
        'songs':Audio.objects.all()
    }
    return render(request,'videos/list2.html',context)

@csrf_exempt
def upload_mp3(request):
    if request.method=="POST":
        uploaded_file = request.FILES['myFile']
        audio=Audio.objects.create(title=request.POST.get('title'),artist=request.POST.get('artist'),path=uploaded_file.name)
        audio.save()
        audio=Audio.objects.all().last()
        id=audio.id
        fs=FileSystemStorage(f'{BASE_DIR}\\media')
        fs.save(f'{id}.mp3',uploaded_file)
        return HttpResponse("Uploaded Successfully!")
    return render(request,'videos/upload_audio.html')

def audio_play_play_by_id(request,id):
    context={
        'song':Audio.objects.get(id=id)
    }
    return render(request,'videos/listen.html',context)
