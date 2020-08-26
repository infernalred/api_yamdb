from rest_framework import viewsets, exceptions, filters, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ViewSetMixin
from rest_framework.generics import DestroyAPIView


class TitleView(viewsets.ModelViewSet):
    permission_classes = (AdminOrReadOnly, IsAdminUser)
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('name', 'year', 'genre', 'category', )

    def perform_create(self, serializer):
        serializer.save()

class GenreView(ViewSetMixin, generics.ListCreateAPIView):

    permission_classes = (AdminOrReadOnly, IsAdminUser)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]

    

class CategoryView(ViewSetMixin, generics.ListCreateAPIView):
    permission_classes = (AdminOrReadOnly, IsAdminUser)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]

    