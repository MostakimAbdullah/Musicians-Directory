from django.urls import path
from . import views

urlpatterns =[
    #path('add/', views.musician, name='add_musician'),
    path('add/', views.MUSICIANVIEW.as_view(), name='add_musician'),
    #path('delete/<int:id>', views.delete, name='delete'),
    path('delete/<int:id>', views.DELETEVIEW.as_view(), name='delete'),
    #path('edit_musician/<int:id>', views.update_musician, name='edit_musician'),
    path('edit_musician/<int:id>', views.UPDATEMUSICIANVIEW.as_view(), name='edit_musician'),
]