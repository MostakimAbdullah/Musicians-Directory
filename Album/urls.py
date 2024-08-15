from django.urls import path
from . import views

urlpatterns =[
    path('add/', views.Album , name='add_album'),
    path('edit/<int:id>', views.edit, name='edit'),
    
]