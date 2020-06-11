from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView

from banner.models import Banner
from banner.serializers import BannerSerializer


class BannersView(ListAPIView, CreateAPIView):

    serializer_class = BannerSerializer

    queryset = Banner.objects.all()


class BannerView(RetrieveUpdateDestroyAPIView):
    serializer_class = BannerSerializer

    queryset = Banner.objects.all()
