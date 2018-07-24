from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    feed  = models.CharField(max_length=200)
    
