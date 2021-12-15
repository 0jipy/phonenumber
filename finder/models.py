from django.db import models

# Create your models here.

class Finder(models.Model):
    name = models.CharField(max_length=20)
    age  = models.CharField(max_length=20)
    birth= models.DateField()
    email= models.CharField(max_length=30)

    def __str__(self):
        return f'[{self.pk}] {self.name}  :  {self.email}'

    def get_absolute_url(self):
        return f'/finder/{self.pk}/'