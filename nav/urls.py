from django.urls import re_path

from nav import views

urlpatterns = [
    re_path('nav_menu/$', views.NavMenusView.as_view()),
    re_path('nav_menu/(?P<pk>\d+)/$', views.NavMenuView.as_view(), name='navmenu-detail')
]