from django.shortcuts import get_object_or_404, render
from youtubers.models import Youtuber

# Create your views here.

def youtubers(request):
    youtubers = Youtuber.objects.order_by("-created_date")
    data={
        'youtubers':youtubers
    }
    return render(request,'youtubers/tubers.html',data)

def youtubers_detail(request,id):
    tuber= get_object_or_404(Youtuber,pk=id)
    data={
            'tuber':tuber,
        }
    return render(request,'youtubers/tuberdetails.html',data)

def search(request):
    pass
