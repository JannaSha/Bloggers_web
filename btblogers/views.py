# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response
from .models import DiscriptionBlogers, Types, Products, Video, Brands
from django.conf import settings
import random

IMG_SIZE = {'height': 400, 'width': 530}


def show_home_page(request):
    port = 'http://127.0.0.1:8000/btblogers/'
    list_blogers = DiscriptionBlogers.objects.all()
    errors = []
    blogers = []
    products = []
    brands = []
    videos = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Поисковой запрос не был задан.')
        else:
            blogers = DiscriptionBlogers.objects.filter(nikname__icontains=q)
            products = Products.objects.filter(name__icontains=q)
            brands = Brands.objects.filter(name__icontains=q)
            videos = Video.objects.filter(video_name__icontains=q)
    context = {'errors': errors, 'blogers': blogers, 'products':products, 
                    'brands':brands, 'videos':videos, 'list_blogers':list_blogers}
    return render_to_response('btblogers/home_page.html', context)

def show_list_blogers(request):
    list_blogers = DiscriptionBlogers.objects.all()
    context = {'list_blogers':list_blogers}
    return render(request, 'btblogers/bloger.html', context)


def get_list_type(type_id):
    list_product = get_object_or_404(Types, pk=type_id)
    return list_product


def show_bloger(request, name):
    bloger = get_object_or_404(DiscriptionBlogers, nikname=name)
    video_list = Video.objects.filter(id_blogers=bloger.id)

    number_video = random.randint(0, len(video_list) - 1)
    context = {'bloger':bloger, 'video_list':video_list, 
                'img_size':IMG_SIZE, 'number_video':number_video}
    return render(request, 'btblogers/blogrer_dis.html', context)


def show_product_list(request):
    list_Type = Types.objects.all()
    dic_all_types = {}
    for i in range(0, len(list_Type)):
        dic_all_types[list_Type[i].type_name] = Products.objects.filter(type_name=i+1)
    context = {'product_dictionary':dic_all_types}
    return render(request, 'btblogers/product_list.html', context)


def show_product(request, id_p):
    product = get_object_or_404(Products, id=id_p)
    context = {'product':product}
    return render(request, 'btblogers/product_dis.html', context)


def show_video(request, id_v):
    video = get_object_or_404(Video, id=id_v)
    context = {'video':video}
    return render(request, 'btblogers/video_dis.html', context)


def show_video_list(request):
    list_video = Video.objects.all()
    context = {'video_list':list_video}
    return render(request, 'btblogers/video_list.html', context)

def show_brands_list(request):
    list_brand = Brands.objects.all()
    size_img = {'height':100, 'width':180}
    context = {'brands_list':list_brand, 'img_size':size_img}
    return render(request, 'btblogers/brands_list.html', context)




