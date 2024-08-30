from django.shortcuts import render,redirect
from Album.models import Album
from django.views.generic import ListView


def home(request):
    data=Album.objects.all()
    return render(request, 'base.html', {'data': data})

class HomeView(ListView):
    model = Album
    template_name = 'base.html'
    context_object_name = 'data'