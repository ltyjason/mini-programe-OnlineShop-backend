# coding=utf-8
from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from goods.models import GoodTypes, GoodType, Goods, GoodDetail, GoodAutoImg, isLike


@admin.register(GoodTypes)
class GoodTypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'ishaveChild')
    list_display_links = ['name']
    actions = None
    ordering = ['id']


@admin.register(GoodType)
class GoodTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_name', 'show_img')
    list_display_links = ['id', 'name', 'get_name', 'show_img']
    ordering = ['id']
    list_filter = ['parent_category']
    search_fields = ['^parent_category__name']
    readonly_fields = ['show_img']
    list_per_page = 10

    def show_img(self, obj):
        return format_html(
            '<img src="http://{}" width="50px"/>',
            obj.imgurl
        )

    def get_name(self, obj):
        return obj.parent_category.name

    show_img.short_description = u"分类图片"
    get_name.short_description = u'父类目级别'


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name', 'show_img', 'g_price', 'get_name')
    list_display_links = ['id', 'short_name', 'show_img', 'g_price', 'get_name']
    readonly_fields = ['show_img']
    list_filter = ['parent_category']
    ordering = ['id']

    def short_name(self, obj):
        if len(str(obj.g_name)) > 20:
            return '{}...'.format(str(obj.g_name)[0:20])
        else:
            return str(obj.g_name)

    def show_img(self, obj):
        return format_html(
            '<img src="{}" width="100px"/>',
            obj.g_imgs
        )

    def get_name(self, obj):
        return obj.parent_category.name

    short_name.short_description = u"商品名称"
    show_img.short_description = u'商品封面图'
    get_name.short_description = u'父类商品'


@admin.register(GoodDetail)
class GoodDetailAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'show_each_detail', 'price')
    list_display_links = ['short_name', 'price']
    readonly_fields = ['show_each_detail']
    ordering = ['id']

    def show_each_detail(self, obj):
        imgs = obj.details.split(";")
        for img in imgs:
            return format_html(
                '<img src="{}" width="100px" display="flex"/>', img,
            )

    def short_name(self, obj):
        if len(str(obj.name)) > 20:
            return '{}...'.format(str(obj.name)[0:20])
        else:
            return str(obj.name)

    short_name.short_description = u'商品简介'
    show_each_detail.short_description = u'详情图片'


@admin.register(GoodAutoImg)
class GoodAutoImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'show_img', 'short_name')
    list_display_links = ['id', 'show_img', 'short_name']
    ordering = ['id']
    list_filter = ['parent_category']
    readonly_fields = ['show_img']
    search_fields = ['^parent_category__name']
    list_per_page = 20

    def show_img(self, obj):
        return format_html(
            '<img src="{}" width="100px"/>',
            obj.imgUrl
        )

    def short_name(self, obj):
        if len(str(obj.parent_category)) > 20:
            return '{}...'.format(str(obj.parent_category)[0:20])
        else:
            return str(obj.parent_category)

    show_img.short_description = u'商品图片'
    short_name.short_description = u'父类目级别'


@admin.register(isLike)
class isLikeAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'good_img', 'like')
    list_display_links = None
    ordering = ['id']
    list_filter = ['user_id__nickname']
    actions = None
    search_fields = ['^user_id__nickname']
    readonly_fields = ['user_name']

    # def get_list_display(self, request):
    #     return ['user_name', 'good_img', 'like']

    def good_img(self, obj):
        return format_html(
            '<img src="{}" width="100px"/>',
            obj.good_id.g_imgs
        )

    def user_name(self, obj):
        return obj.user_id.nickname

    good_img.short_description = u'关联商品id'
    user_name.short_description = u'关联用户id'



