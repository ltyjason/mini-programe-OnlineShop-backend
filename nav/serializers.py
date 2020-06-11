from rest_framework import serializers

from nav.models import NavMenu


class NavSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = NavMenu
        fields = ('url', 'id', 'menuName', 'n_img')