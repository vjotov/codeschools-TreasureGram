from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name = 'home'),
    url(r'^$', views.index, name = 'index'),
    url(r'^([1-9])+/$', views.datail, name = 'detail'),
    url(r'^post_url/$', views.post_treasure, name = 'post_treasure'),
]
