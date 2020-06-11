from django.urls import path, re_path

from user import views

urlpatterns = [
    path('user', views.UserView.as_view()),
]