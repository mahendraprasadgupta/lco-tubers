from django.db import models
from datetime import datetime

# Create your models here.
class Hiretuber(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    message = models.TextField(max_length=255,blank=True)
    
    user_id = models.IntegerField(blank=True)
    
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=100)
    
    
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email