from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^$', views.index, name = 'index'),
    url(r'^([1-9])+/$', views.datail, name = 'detail'),
    url(r'^post_url/$', views.post_treasure, name = 'post_treasure'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(<?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT,}),

    ]
