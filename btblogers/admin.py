from django.contrib import admin

from .models import DiscriptionBlogers, Types, Products, Comments, Video, Brands

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name',  'name', 'type_name', 'price', 'foto')


class BlogersAdmin(admin.ModelAdmin):
	list_display = ('id', 'nikname', 'sur_name', 'firs_name', 'country', 'city', 'foto')


class TypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'type_name')
	search_fields = ('type_name', )

class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'author', 'id_bloger', 'comment')


class VideoAdmin(admin.ModelAdmin):
	list_display = ('id', 'video_name')


class BrandsAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'url', 'image')

admin.site.register(DiscriptionBlogers, BlogersAdmin)
admin.site.register(Types, TypeAdmin)
admin.site.register(Products, ProductAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Brands, BrandsAdmin)

