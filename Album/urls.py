from django.urls import path
from . import views

urlpatterns =[
    #path('add/', views.Album , name='add_album'),
    path('add/', views.ALBUMVIEW.as_view() , name='add_album'),
    #path('edit/<int:id>', views.edit, name='edit'),
    path('edit/<int:id>', views.EDITVIEW.as_view(), name='edit'),
    
]