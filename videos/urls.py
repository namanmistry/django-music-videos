
from django.urls import path
from .views import home,upload,player,audio_player,upload_mp3,audio_play_play_by_id

urlpatterns = [
    path('', home),
    path('upload/', upload),
    path('upload/audio/', upload_mp3),
    path('play/<int:id>/', player),
    path('audio/<int:id>/', audio_play_play_by_id),
    path('audio/', audio_player),

]