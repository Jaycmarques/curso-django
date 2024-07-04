from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('videos:video', args=(self.slug,))


videos = [
    Video('motivacao', 'Video: Motivação', 973584504),
    Video('instalacao-windows', 'Instalação Windows', 1234567),
]

videos_dic = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'videos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dic[slug]
    return render(request, 'videos/video.html', context={'video': video})
