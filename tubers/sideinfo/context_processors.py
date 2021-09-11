from . models import HeaderSideinfo,FooterSideinfo

def extras(request):

    headersideinfo = HeaderSideinfo.objects.order_by('-created_date').filter(active = True)[0]
    data={
        'headersideinfo':headersideinfo,
    }
    return data