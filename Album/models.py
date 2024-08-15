from django.db import models
from Musician.models import Musicians
from django.utils import timezone
# Create your models here.
class Album(models.Model):
    artist = models.ForeignKey(Musicians, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateTimeField(auto_now_add=True)
    Choices =[
        ( 1, '1'),
        (2, '2'),
        ( 3, '3'),
        (4, '4'),
        ( 5, '5')
    ]
    rating = models.IntegerField(choices=Choices)


    def __str__(self):
        return self.name
