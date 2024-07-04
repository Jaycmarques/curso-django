from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video: Motivação', 'vimeo_id': 973584504},
        'instalacao-windows': {'titulo': 'Instalação Windows', 'vimeo_id': 1234567},
    }
    video = videos[slug]
    return render(request, 'videos/video.html', context={'video': video})
