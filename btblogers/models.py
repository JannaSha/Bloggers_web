from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class DiscriptionBlogers(models.Model):
    """ Table contains information about blogers """
    nikname = models.CharField(max_length=30)
    sur_name = models.CharField(max_length=15, null=True, default=None)
    firs_name = models.CharField(max_length=15)
    age = models.PositiveSmallIntegerField(null=True, default=None)
    country = models.CharField(max_length=30, null=True, default=None)
    city = models.CharField(max_length=30, null=True, default=None)
    url_instagramm = models.URLField(null=True, default=None)
    url_youtube = models.URLField()
    foto = models.ImageField(upload_to='blogers', blank=True)
    discription = models.TextField()

    def get_absolute_url(self):
        return "/btblogers/bloger/%s/" % self.nikname

    def __unicode__(self):
        return self.nikname


class Types(models.Model):
    """ Type of cosmetic products """
    type_name =  models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.type_name

class Comments(models.Model):
    """
    Table contains comment and
    comment's author information 
    """
    comment = models.TextField()
    author = models.CharField(max_length=50, null=True, default=None)
    id_bloger = models.ForeignKey(DiscriptionBlogers, null=True, blank=True, default=None)
    date_comment = models.DateTimeField('Date of published')

    def __unicode__(self):
        return self.comment

class Products(models.Model):
    """ 
    Table contains information 
    about cosmetic products
    """
    brand_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=25, null=True, default=None, blank=True)
    type_name = models.ForeignKey(Types)
    mark = models.FloatField(default=0)
    price = models.FloatField(null=True, default=None, blank=True)
    foto = models.ImageField(upload_to='products', null=True, blank=True,
                                default=settings.DEFAULT_PRODUCT_IMG)
    url = models.URLField(null=True, default=None, blank=True)
    additional_info = models.TextField(null=True, default=None, blank=True)
    id_comments = models.ManyToManyField(Comments, blank=True, related_name='com_product')

    def get_absolute_url(self):
        return "/btblogers/product/%i/" % self.id

    def get_comment_url(self):
        return "btblogers/comment/new/%i" % self.id

    def __unicode__(self):
        return self.name


class Video(models.Model):
    """
    Information about video with 
    and cosmetic product in each video
    """
    id_blogers = models.ManyToManyField(DiscriptionBlogers, related_name='video')
    date_video = models.DateTimeField()
    video_name = models.CharField(max_length=100)
    id_good_products = models.ManyToManyField(Products, related_name='rel_GP', blank=True, default=None)
    id_bad_products = models.ManyToManyField(Products, related_name='rel_BP', blank=True, default=None)
    url_youtube = models.URLField(default=None)
    discription_video = models.TextField(null=True, blank=True, default=None)
    html_video = models.CharField(max_length=200, null=True, blank=True, default=None)

    def get_absolute_url(self):
        return "/btblogers/video/%i/" % self.id


class Brands(models.Model):
    """
    This calss contaun discription about 
    all brands for product list
    """
    name = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True, default=None)
    image = models.ImageField(upload_to='brands', null=True, blank=True,
                                default=settings.DEFAULT_BRANDS_IMG)


