from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from nav.models import NavMenu
from nav.serializers import NavSerializers


class NavMenusView(ListAPIView, CreateAPIView):

    serializer_class = NavSerializers

    queryset = NavMenu.objects.all()


class NavMenuView(RetrieveUpdateDestroyAPIView):

    serializer_class = NavSerializers

    queryset = NavMenu.objects.all()
