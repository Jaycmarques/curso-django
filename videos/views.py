from django.shortcuts import render


def video(request, slug):
    return render(request, 'videos/video.html')
