from django.db import models

# Create your models here.
class HeaderSideinfo(models.Model):
    
    email  = models.CharField(max_length=100,blank=False)
    mobile = models.CharField(max_length=100,blank=False)
    signin = models.CharField(max_length=10,blank=False)
    signup = models.CharField(max_length=10,blank=False)
    active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)


class FooterSideinfo(models.Model):
    sec1_msg1 = models.CharField(max_length=255)
    sec1_button = models.CharField(max_length=255)

    sec2_msg2 = models.CharField(max_length=255)
    copyrightmsg = models.CharField(max_length=100,blank=True)
    facebook_url = models.CharField(max_length=255,blank=True)
    twitter_url = models.CharField(max_length=255,blank=True)
    instagram_url = models.CharField(max_length=255,blank=True)
    youtube_url = models.CharField(max_length=255,blank=True)
    active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
