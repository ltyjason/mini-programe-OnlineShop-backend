from rest_framework import serializers

from goods.models import GoodTypes, GoodType, Goods, GoodDetail, GoodAutoImg, isLike


class GoodTypeSerializer2(serializers.ModelSerializer):

    class Meta:
        model = GoodType
        fields = "__all__"


class GoodTypeSerializer(serializers.ModelSerializer):

    ClassifyList = GoodTypeSerializer2(many=True)

    class Meta:
        model = GoodTypes
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = "__all__"


class DetailSerializer2(serializers.ModelSerializer):

    class Meta:
        model = GoodAutoImg
        fields = "__all__"


class DetailSerializer(serializers.ModelSerializer):

    shopGoodsImageList = DetailSerializer2(many=True)

    class Meta:
        model = GoodDetail
        fields = "__all__"


class isLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = isLike
        fields = "__all__"


class searchSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodDetail
        fields = "__all__"
