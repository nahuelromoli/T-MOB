from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.views.decorators.http import require_http_methods
from .common.helper import get_url
import json
from .models import Redirect
from django.core.cache import cache



@require_http_methods(["GET"])
def view_redirect(request, key):
    try:
        url = get_url(key)
        if url:
            data = {"key": key, "url": url }
            return HttpResponse(json.dumps(data),content_type='application/json',status=200)
        return HttpResponseBadRequest('The key not exist')
    except:
        return HttpResponseServerError('Internal error')    

@require_http_methods(["GET"])
def delete_redirect(request,id):
    try:
        redirect =  Redirect.objects.get(id=id)
        if cache.has_key(redirect.key): cache.delete(redirect.key)
        redirect.delete()
        return HttpResponse("Successfully removed",status=200)
    except:
        return HttpResponseBadRequest('ID not exist')