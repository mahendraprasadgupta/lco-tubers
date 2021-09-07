from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Youtuber(models.Model):

    crew_choices =(
        ('solo','solo'),
        ('small','small'),
        ('large','large'),
    )

    camera_choices =(
        ('canon','canon'),
        ('nikon','nikon'),
        ('sony','sony'),
        ('Red','Red'),
        ('fuji','fuji'),
        ('panasonic','panasonic'),
        ('others','others'),
    )

    catagory_choices =(
        ('code','code'),
        ('cooking','cooking'),
        ('mobile_review','mobile_review'),
        ('vlogs','vlogs'),
        ('comedy','comedy'),
        ('gaming','gaming'),
        ('film_making','film_making'),
    )


    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/ytubers/%Y/%m')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices,max_length=255)
    camera_type = models.CharField(choices=camera_choices,max_length=255)
    sub_count = models.CharField(max_length=255)
    category = models.CharField(choices=catagory_choices,max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now,blank=True)

