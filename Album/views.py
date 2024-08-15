from django.shortcuts import render,redirect
from Album.forms import add_Album
from . import models

# Create your views here.
def Album(request):
    if request.method == 'POST':
        form = add_Album(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_album')
    else:
        form = add_Album()
    return render(request, 'add_album.html', {'form': form})


def edit(request,id):
    album = models.Album.objects.get(pk=id)
    form = add_Album(instance=album)
    if request.method == 'POST':
        form = add_Album(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')    
    return render(request, 'add_album.html', {'form': form})

