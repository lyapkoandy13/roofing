from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^ajax/check/user/$', views.check_user, name='check_user'),
    url(r'^ajax/remove_good/$', views.ajax_remove_good, name='ajax_remove_good'),
    url(r'^ajax/move_up/$', views.ajax_move_up, name='ajax_move_up'),
    url(r'^ajax/move_down/$', views.ajax_move_down, name='ajax_move_down'),
    url(r'^add_good/', views.add_good, name='add_good'),
    url(r'^edit_good/', views.edit_good, name='edit_good'),
]