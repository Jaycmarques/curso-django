from django.shortcuts import render
from videos.models import Video


videos = [
    Video(slug='motivacao', titulo='Video: Motivação', vimeo_id='973584504'),
    Video(slug='instalacao-windows',
          titulo='Instalação Windows', vimeo_id='1234567'),
]

videos_dic = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'videos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dic[slug]
    return render(request, 'videos/video.html', context={'video': video})
