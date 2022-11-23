from django.urls import path
from . import views

urlpatterns = [
     path('<str:key>', views.view_redirect),
     path('<int:id>/',  views.delete_redirect)
]