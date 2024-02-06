import json
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import IPAddress
from django.template import loader

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def store_info(request):
    ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    referrer = request.META.get('HTTP_REFERER', '')
    host = request.get_host()
    path = request.path
    method = request.method
    cookies = request.COOKIES
    session_data = request.session

    ip_address_entry = IPAddress.objects.create(
        ip_address=ip, 
        user_agent=user_agent,
        referrer=referrer,
        host=host,
        path=path,
        method=method,
        cookies=cookies,
        session_data=session_data
    )

    template = loader.get_template("iplogs/index.html")

    request.session['ip_address_entry_id'] = ip_address_entry.id

    return HttpResponse(template.render(request=request))

@csrf_exempt
def store_location(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        lat = data.get('latitude')
        lon = data.get('longitude')

        ip_address_entry_id = request.session.get('ip_address_entry_id')

        if ip_address_entry_id is not None:
            try:
                ip_address_entry = IPAddress.objects.get(id=ip_address_entry_id)
            except IPAddress.DoesNotExist:
                ip_address_entry = IPAddress.objects.create(latitude=lat, longitude=lon)
                request.session['ip_address_entry_id'] = ip_address_entry.id
        else:
            ip_address_entry = IPAddress.objects.create(latitude=lat, longitude=lon)
            request.session['ip_address_entry_id'] = ip_address_entry.id

        ip_address_entry.latitude = lat
        ip_address_entry.longitude = lon
        ip_address_entry.save()

        return JsonResponse({'status': 'success'})
    
# utility function to get client's IP
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
