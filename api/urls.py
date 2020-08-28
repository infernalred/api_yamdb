from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ReviewViewSet, CommentViewSet, TitleView, GenreView, CategoryView

router_v1 = DefaultRouter()
router_v1.register(r'titles', TitleView, basename='titles')
router_v1.register('genres', GenreView, basename='genres')
router_v1.register('categories', CategoryView, basename='categories')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='Review')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
                   CommentViewSet, basename='Comment')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]