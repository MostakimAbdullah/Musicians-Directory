from django.urls import path
from . import views

urlpatterns =[
    path('add/', views.musician, name='add_musician'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit_musician/<int:id>', views.update_musician, name='edit_musician'),
]