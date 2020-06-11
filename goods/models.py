# coding=utf-8
from django.db import models

from user.models import WxUser


class ClassifyList(models.Model):

    name = models.CharField(verbose_name=u'分类名', max_length=16)

    class Meta:
        abstract = True


class GoodTypes(ClassifyList):

    ishaveChild = models.BooleanField(verbose_name=u'类目级别', default=False)

    class Meta:
        db_table = 'good_types'
        verbose_name = '导航类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodType(ClassifyList):

    parent_category = models.ForeignKey(GoodTypes, verbose_name=u"父类目级别", null=True, blank=True,
                                        related_name="ClassifyList", on_delete=models.CASCADE)
    imgurl = models.CharField(verbose_name=u'分类图片', max_length=256, null=True)

    class Meta:
        db_table = 'good_type'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):

    g_name = models.CharField(verbose_name=u'商品名称', max_length=128)
    g_imgs = models.CharField(verbose_name=u'商品封面图', max_length=1024)
    g_price = models.FloatField(verbose_name=u'价格', default=0)
    parent_category = models.ForeignKey(GoodType, verbose_name=u'父类商品', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'goods'
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.g_name


class shopGoodsImageList(models.Model):

    imgUrl = models.CharField(verbose_name=u'商品图片', max_length=2048)

    class Meta:
        abstract = True


class GoodDetail(shopGoodsImageList):

    name = models.CharField(verbose_name=u'商品简介', max_length=128)
    parent_category = models.ForeignKey(Goods, verbose_name=u"父类目级别", null=False, blank=True,
                                        on_delete=models.CASCADE, default='')
    details = models.TextField(verbose_name=u'详情图片', max_length=2048)
    price = models.FloatField(verbose_name=u'商品价格', default=0)

    class Meta:
        db_table = 'GoodDetail'
        verbose_name = '商品详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodAutoImg(shopGoodsImageList):

    parent_category = models.ForeignKey(GoodDetail, verbose_name=u"父类目级别", null=False, blank=True,
                                        related_name="shopGoodsImageList", on_delete=models.CASCADE, default='')

    class Meta:
        db_table = 'GoodAutoImg'
        verbose_name = '商品轮播图'
        verbose_name_plural = verbose_name


class isLike(models.Model):
    like_CHOICES = (
        (0, 'False'),
        (1, 'True'),
    )

    good_id = models.ForeignKey(Goods, verbose_name=u'关联商品id', null=False, blank=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(WxUser, verbose_name=u'关联用户id', null=False, blank=True, on_delete=models.CASCADE)
    like = models.BooleanField(choices=like_CHOICES, default=0)

    class Meta:
        db_table = 'isLike'
        verbose_name = '收藏'
        verbose_name_plural = '收藏'





