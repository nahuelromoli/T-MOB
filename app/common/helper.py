
from django.core.cache import cache

def get_url(key):
    try:
        redirect = cache.get(key)
        return redirect.url if redirect else None
    except: 
        raise Exception("Error getting instance")