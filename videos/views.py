from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video: Motivação', 'vimeo_id': 973584504}
    return render(request, 'videos/video.html', context={'video': video})
