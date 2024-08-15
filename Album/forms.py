from django import forms 
from .models import Album

class add_Album(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'