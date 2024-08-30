from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render , redirect
from Musician.forms import add_musician
from . import models
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView,UpdateView

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


class MUSICIANVIEW(CreateView):
    model = models.Musicians
    form_class = add_musician
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')
    def form_valid(self, form):
        return super().form_valid(form)


def delete(request,id):
    album = models.Musicians.objects.get(pk=id)
    album.delete()
    return redirect('home')

class DELETEVIEW(DeleteView):
    model = models.Musicians
    pk_url_kwarg = 'id'
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


def update_musician(request,id):
    album = models.Musicians.objects.get(pk=id)
    form = add_musician(instance=album)
    if request.method == 'POST':
        form = add_musician(request.POST,instance=album)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    return render(request,'add_musician.html', {'form': form})

class UPDATEMUSICIANVIEW(UpdateView):
    model = models.Musicians
    form_class = add_musician
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('add_musician')
    def form_valid(self, form):
        return super().form_valid(form)