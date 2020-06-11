from django.urls import re_path

from banner import views

urlpatterns = [
    re_path('banner/$', views.BannersView.as_view()),
    re_path('banner/(?P<pk>\d+)/$', views.BannerView.as_view(), name='banner-detail')
]
