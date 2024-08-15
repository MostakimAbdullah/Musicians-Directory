from django.shortcuts import render,redirect
from Album.models import Album


def home(request):
    data=Album.objects.all()
    return render(request, 'base.html', {'data': data})