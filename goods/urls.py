from django.urls import re_path, path

from goods import views

urlpatterns = [
    re_path('goodtypes/$', views.GoodTypesView.as_view(), name='goodtypes-detail'),
    re_path('goodtypes/(?P<pk>\d+)/$', views.GoodTypes_View.as_view(), name='goodtypes-detail'),

    re_path('goodtype/$', views.GoodTypeView.as_view(), name='goodtype-detail'),
    re_path('goodtype/(?P<pk>\d+)/$', views.GoodType_View.as_view(), name='goodtype-detail'),

    re_path('goods/$', views.GoodsView.as_view(), name='goods-detail'),
    re_path('goods/(?P<parent_category>\d+)/$', views.Goods_View.as_view(), name='goods-detail'),
    re_path('good/(?P<pk>\d+)/$', views.Good_View.as_view(), name='good-detail'),

    re_path('gooddetails/$', views.GoodDetailView.as_view(), name='gooddetails-detail'),
    re_path('gooddetails/(?P<pk>\d+)/$', views.GoodDetail_View.as_view(), name='gooddetails-detail'),
    re_path('gooddetail/$', views.GoodAutoImgView.as_view(), name='gooddetail-detail'),
    re_path('gooddetail/(?P<parent_category>\d+)/$', views.GoodAutoImg_View.as_view(), name='gooddetail-detail'),

    re_path('islike/$', views.isLikeView.as_view()),
    re_path('islikes/$', views.isLikesView.as_view(),),

    re_path('order/$', views.getOrder.as_view(),),

    re_path('search/$', views.search.as_view(), name='search-detail')
]