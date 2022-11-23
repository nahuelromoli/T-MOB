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
    cache.set(instance.key,instance) if instance.active else cache.delete(instance.key)    

post_save.connect(signal_update, sender = Redirect)