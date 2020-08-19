from django.db import models
from django.utils import timezone

# Create your models here.
class Write(models.Model):
    title=models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', default='ootdapp/defaultimage/ho.jpg')
    pub_date=models.DateTimeField('date published')
    body =models.TextField()

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField('date')

    def __str__(self):
        return self.title