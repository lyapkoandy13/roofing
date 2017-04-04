from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajax/get_goods/$', views.ajax_get_goods, name='ajax_get_goods'),
    url(r'^ajax/get_images/$', views.ajax_get_images, name='ajax_get_images'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)