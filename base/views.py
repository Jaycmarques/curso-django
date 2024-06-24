from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<html><body>Hello World!</body></html>', content_type='text/html')
