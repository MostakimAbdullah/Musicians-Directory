from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from Album.forms import add_Album
from . import models
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView

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

class ALBUMVIEW(CreateView):
    model = models.Album
    form_class = add_Album
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        return super().form_valid(form)



def edit(request,id):
    album = models.Album.objects.get(pk=id)
    form = add_Album(instance=album)
    if request.method == 'POST':
        form = add_Album(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')    
    return render(request, 'add_album.html', {'form': form})

class EDITVIEW(UpdateView):
    model = models.Album
    form_class = add_Album
    pk_url_kwarg = 'id'
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')
