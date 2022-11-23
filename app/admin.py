from django.contrib import admin
from .models import Redirect

@admin.register(Redirect)
class RedirectAdmin(admin.ModelAdmin):
    list_display=('id','url','key','created_at','updated_at','active')
    ordering= ('key',)
    search_fields = ('key','url')
    list_editable = ('key','active')
    list_filter = ('created_at','updated_at','active')
    list_per_page = 8
