from django.db import models


class Musicians(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    instrument=models.CharField(max_length=100)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

