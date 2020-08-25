from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )


router_v1 = DefaultRouter()
router_v1.register(r'titles', TitleView, basename='titles')
router_v1.register('genres', GenreView, basename='genres')
router_v1.register('categories', CategoryView, basename='categories')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]