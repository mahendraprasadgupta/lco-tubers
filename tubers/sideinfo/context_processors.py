from . models import HeaderSideinfo,FooterSideinfo

def extras(request):

    headersideinfo = HeaderSideinfo.objects.order_by('-created_date').filter(active = True)[0]
    footersideinfo = FooterSideinfo.objects.order_by('-created_date').filter(active = True)[0]
    data={
        'headersideinfo':headersideinfo,
        'footersideinfo':footersideinfo,
    }
    return data