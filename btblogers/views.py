# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response
from .models import DiscriptionBlogers, Types, Products, Video, Brands, Comments
from django.conf import settings
from .forms import CommentForm
from django.shortcuts import redirect
import datetime
from django.utils import timezone
import random

IMG_SIZE = {'height': 400, 'width': 530}


def show_home_page(request):
    port = 'http://127.0.0.1:8000/btblogers/'
    list_blogers = DiscriptionBlogers.objects.all()
    errors = []
    blogers = []
    products = []
    brands = []
    video = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Поисковой запрос не был задан.')
        else:
            blogers = DiscriptionBlogers.objects.filter(nikname__icontains=q)
            products = Products.objects.filter(name__icontains=q)
            brands = Brands.objects.filter(name__icontains=q)
            video = Video.objects.filter(video_name__icontains=q)
    context = {'errors': errors, 'blogers': blogers, 'products':products, 
                    'brands':brands, 'video':video, 'list_blogers':list_blogers}
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
    video_list_img = []
    number_video = 0
    video_list_dis = None
    video_list_url = video_list.values('url_youtube')
    for video in video_list_url:
        temp = video.get('url_youtube').split("=")
        string = 'https://img.youtube.com/vi/' + temp[1] + '/0.jpg'
        video_list_img.append(string)
        video_list_dis = []
    for i in range(0, len(video_list_url)):
        dis = {'img_url' : video_list_img[i], 'video_obj':video_list[i]}
        video_list_dis.append(dis)
    context = {'bloger':bloger, 'video_list':video_list_dis, 
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
    product1 = Products.objects.filter(id=id_p)
    comments_id = product1.values('id_comments')
    comments = []
    for comment in comments_id:
        comments.append(Comments.objects.filter(id=comment['id_comments']))
    context = {'product':product, 'comment':comments}
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

def comment_new(request, id_product):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.date_comment = timezone.now()
            comment.save()
            product = get_object_or_404(Products, id=id_product)
            product.id_comments.add(comment.id)
            return redirect('/btblogers/product/' + id_product + '/', id=id_product)
    else:
        form = CommentForm()
    return render(request, 'btblogers/comment_add.html', {'form':form})



