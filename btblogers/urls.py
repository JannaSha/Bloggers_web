from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^blogers_list/$', views.show_list_blogers, name='show_list_blogers'),
    url(r'^product_list/$', views.show_product_list, name='show_product_list'),
   	url(r'^bloger/(?P<name>[a-zA-Z0-9-_]+)/$', views.show_bloger, name='show_bloger'),
    url(r'^product/(\d{1,1000})/$', views.show_product, name='show_product'),
    url(r'^video/(\d{1,10000})/$', views.show_video, name='show_video'),
    url(r'^video_list/$', views.show_video_list, name='show_video_list'),
    url(r'^brands_list/$', views.show_brands_list, name='show_brands_list'),
    url(r'^index/$', views.show_home_page, name='index'),
    url(r'comment/new/(\d{1,10000})/$', views.comment_new, name='comment_new'),
   
]


