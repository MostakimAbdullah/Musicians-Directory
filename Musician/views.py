from django.shortcuts import render , redirect
from Musician.forms import add_musician
from . import models

# Create your views here.
def musician(request):
    if request.method == 'POST':
        form = add_musician(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:
        form = add_musician()
    return render(request,'add_musician.html', {'form': form})


def delete(request,id):
    album = models.Musicians.objects.get(pk=id)
    album.delete()
    return redirect('home')


def update_musician(request,id):
    album = models.Musicians.objects.get(pk=id)
    form = add_musician(instance=album)
    if request.method == 'POST':
        form = add_musician(request.POST,instance=album)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    return render(request,'add_musician.html', {'form': form})