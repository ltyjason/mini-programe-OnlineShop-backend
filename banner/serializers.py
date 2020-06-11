from rest_framework import serializers

from banner.models import Banner


class BannerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Banner
        fields = ('url', 'id', 'b_name', 'b_img', 'type')