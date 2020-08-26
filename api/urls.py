from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ReviewViewSet, CommentViewSet

router_v1 = DefaultRouter()
router_v1.register(r'titles/(?P<id>\d+)/reviews', ReviewViewSet, basename='Review')
router_v1.register(r'titles/(?P<id>\d+)/reviews/(?P<id>\d+)/comments', CommentViewSet, basename='Comment')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]