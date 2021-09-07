from django.contrib import admin
from . models import Youtuber
from django.utils.html import format_html


# Register your models here.
class YoutuberAdmin(admin.ModelAdmin):

    def myphoto(self,object):
        return format_html('<img src="{}" width="40px"/>'.format(object.photo.url))


    list_display = ('id','name','category','created_date','myphoto','is_featured')
    list_display_links = ('name',)
    search_fields = ('name','category')
    list_filter = ('category',)
    list_editable = ('is_featured',)

admin.site.register(Youtuber,YoutuberAdmin)
