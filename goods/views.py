# coding=utf-8
from django.http import JsonResponse, QueryDict
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, \
    DestroyAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.utils import json
from rest_framework.views import APIView

from goods.models import GoodTypes, Goods, GoodType, GoodDetail, GoodAutoImg, isLike
from goods.serializers import GoodTypeSerializer, GoodTypeSerializer2, GoodsSerializer, DetailSerializer, \
    DetailSerializer2, isLikeSerializer

#  左导航及对应类型，单显示不可修改
from user.models import WxUser
from user.serializer import UserSerializer


class GoodTypesView(ListAPIView):

    serializer_class = GoodTypeSerializer

    queryset = GoodTypes.objects.filter(ishaveChild=True)


# 按id选择类型，单个id类型的添加、更新、修改和删除
class GoodTypes_View(RetrieveUpdateDestroyAPIView):

    serializer_class = GoodTypeSerializer

    queryset = GoodTypes.objects.all()


# 显示所有类型，可以创建新类型
class GoodTypeView(ListAPIView, CreateAPIView):

    serializer_class = GoodTypeSerializer2

    queryset = GoodType.objects.all()


# 单个类型， 单个id类型的更新和删除
class GoodType_View(RetrieveUpdateDestroyAPIView):

    serializer_class = GoodTypeSerializer2

    queryset = GoodType.objects.all()


# 商品分页器
class GoodPaginations(PageNumberPagination):

    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 10


# 显示所有的商品，可以添加
class GoodsView(ListAPIView, CreateAPIView):

    serializer_class = GoodsSerializer
    pagination_class = GoodPaginations
    queryset = Goods.objects.all()


# 按父类分类商品
class Goods_View(ListAPIView):

    serializer_class = GoodsSerializer
    pagination_class = GoodPaginations

    def get_queryset(self):
        parent_category = self.kwargs['parent_category']
        print(self.kwargs)
        return Goods.objects.filter(parent_category=parent_category)


# 按id筛选商品， 可更新、删除。
class Good_View(RetrieveUpdateDestroyAPIView):

    serializer_class = GoodsSerializer

    queryset = Goods.objects.all()


class GoodDetailView(ListAPIView):

    serializer_class = DetailSerializer

    queryset = GoodDetail.objects.all()


class GoodDetail_View(RetrieveUpdateDestroyAPIView):

    serializer_class = DetailSerializer

    queryset = GoodDetail.objects.all()


class GoodAutoImgView(ListAPIView):

    serializer_class = DetailSerializer2

    queryset = GoodAutoImg.objects.all()


class GoodAutoImg_View(ListAPIView):

    serializer_class = DetailSerializer2

    def get_queryset(self):
        parent_category = self.kwargs['parent_category']
        return GoodAutoImg.objects.filter(parent_category=parent_category)


class isLikeView(APIView):

    def post(self, request, *args, **kwargs):
        uuid = request.data['uuid']
        goodsid = request.data['goodid']

        user = WxUser.objects.get(uuid=uuid).id
        goods = Goods.objects.get(id=goodsid).id
        # print(user.id, goods.id)
        islike = isLike
        like_id = islike.objects.filter(user_id_id=user).filter(good_id_id=goods)
        if like_id.exists():
            like_id = like_id.first()
            like_id.like = bool(1-like_id.like)
            like_id.save()
        else:
            islike.objects.create(user_id_id=user, good_id_id=goods,)

        return Response("Success")

    def get(self, request):
        uuid = request.GET['uuid']
        # print(uuid)
        goodsid = request.GET['goodid']
        user = WxUser.objects.get(uuid=uuid).id
        # print(user)
        goods = Goods.objects.get(id=goodsid).id
        likes = isLike.objects.filter(user_id_id=user).filter(good_id_id=goods)
        # print(likes.values())
        data = []
        for i in likes.values():
            data.append(i)
        print(data)
        return JsonResponse(data, safe=False)


class isLikesView(APIView):

    def get(self, request):
        uuid = request.GET['uuid']
        user = WxUser.objects.get(uuid=uuid).id
        likes = isLike.objects.filter(user_id_id=user).filter(like=True).all()
        print(likes)
        data = []
        for i in likes.values():
            id = i['good_id_id']
            good = Goods.objects.filter(id=id).all()
            for i in good.values():
                data.append((i))
        # print(data)
        return JsonResponse(data, safe=False)


class getOrder(APIView):

    def post(self, request):

        for i in request.data['cart']:
            print(i['name'])
        return Response("")


class search(APIView):

    def post(self, request):
        name = request.GET['title']
        good = Goods.objects.filter(parent_category=1)
        print(good)
        return Response("")