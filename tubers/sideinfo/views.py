from django.shortcuts import render
from . models import HeaderSideinfo

# Create your views here.

def sideinfo(request):
    headersideinfo = HeaderSideinfo.objects.order_by('-created_date').filter(active = True)[0]
    data={
        'headersideinfo':headersideinfo,
    }
    return render(request,'includes/header.html',data)
