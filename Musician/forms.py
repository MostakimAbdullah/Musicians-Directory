from django import forms
from .models import Musicians


class add_musician(forms.ModelForm):
    class Meta:
        model = Musicians
        fields = '__all__'
        