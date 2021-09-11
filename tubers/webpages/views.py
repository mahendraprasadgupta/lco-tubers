from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber

# Create your views here.

teams = Team.objects.all()

def home(request):
    sliders = Slider.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    youtubers = Youtuber.objects.order_by('-created_date')
    data = {
        'sliders':sliders,
        'teams':teams,
        'title':'Home',
        'youtubers':youtubers,
        'featured_youtubers':featured_youtubers
    }
    return render(request,'webpages/home.html',data)

def about(request):
    data = {
        'title':'About',
        'teams':teams,
    }
    return render(request,'webpages/about.html',data)

def contact(request):
    data = {
        'title':'Contact',
    }
    return render(request,'webpages/contact.html',data)

def services(request):
    data = {
        'title':'Services',
    }
    return render(request,'webpages/services.html',data)