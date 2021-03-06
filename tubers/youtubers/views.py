from django.shortcuts import get_object_or_404, render
from youtubers.models import Youtuber
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def youtubers(request):
    
    youtubers = Youtuber.objects.order_by("-created_date").all()
    p = Paginator(youtubers, 2)  
    page_number = request.GET.get('page')

    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:

        page_obj = p.page(1)
    except EmptyPage:
       
        page_obj = p.page(p.num_pages)



    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()

    
    data={
        'page_obj':page_obj,
        'city_search':city_search,
        'camera_search':camera_search,
        'title':'Tubers',
        'category_search':category_search,
    
    }
    return render(request,'youtubers/tubers.html',data)

def youtubers_detail(request,id):
    tuber= get_object_or_404(Youtuber,pk=id)
    data={
            'tuber':tuber,
            'title':tuber.name,
        }
    return render(request,'youtubers/tuberdetails.html',data)

def search(request):
    tubers = Youtuber.objects.order_by("-created_date")
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
    if 'camera' in request.GET:
        camera = request.GET['camera']
        if camera:
            tubers = tubers.filter(camera_type__iexact=camera)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)
    data={
            'tubers':tubers,
            'title':'Search',
            'city_search':city_search,
            'camera_search':camera_search,
            'category_search':category_search,
        }
    return render(request,'youtubers/search.html',data)

