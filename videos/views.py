from django.shortcuts import render

videos = [
    {'slug': 'motivacao', 'titulo': 'Video: Motivação', 'vimeo_id': 973584504},
    {'slug': 'instalacao-windows', 'titulo': 'Instalação Windows', 'vimeo_id': 1234567},
]

videos_dic = {dic['slug']: dic for dic in videos}


def indice(request):
    return render(request, 'videos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dic[slug]
    return render(request, 'videos/video.html', context={'video': video})
