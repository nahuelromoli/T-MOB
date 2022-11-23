from django.db import models
from django.db.models.signals import post_save
from django.core.cache import cache

class Redirect (models.Model):
    key = models.CharField(max_length=50, unique=True)
    url = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.key

    class Meta:
        db_table = 'redirect'
        ordering = ['key']

def signal_update(sender, instance, **kwars):
    actives = Redirect.objects.filter(active=True)
    actives_dictionary = {}
    for ac in actives:
        actives_dictionary[ac.key] = ac
    cache.set_many(actives_dictionary)
    if not instance.active : cache.delete(instance.key)    

post_save.connect(signal_update, sender = Redirect)