from django.urls import path, include

urlpatterns = [
    path('server/', include("banner.urls")),
    path('server/', include("nav.urls")),
    path('server/', include("goods.urls")),
    path('auth/', include("user.urls")),
]