from rest_framework import viewsets, generics, filters
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend

from api.models import Review, Title, Genre, Category, Comment
from api.permissions import AdminOrReadOnly, IsAdminUser
from api.serializers import CommentSerializer, ReviewSerializer, \
    TitleSerializer, GenreSerializer, CategorySerializer


class TitleView(viewsets.ModelViewSet):
    permission_classes = (AdminOrReadOnly, IsAdminUser)
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'year', 'genre', 'category',)

    def perform_create(self, serializer):
        serializer.save()


class GenreView(ViewSetMixin, generics.ListCreateAPIView):
    permission_classes = (AdminOrReadOnly, IsAdminUser)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class CategoryView(ViewSetMixin, generics.ListCreateAPIView):
    permission_classes = (AdminOrReadOnly, IsAdminUser)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (AdminOrReadOnly, IsAdminUser)

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title.objects, pk=title_id)
        queryset = title.reviews.all()
        return queryset

    def perform_create(self, serializer):
        """Create a new comment."""
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title.objects, pk=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        review_id = self.kwargs.get("review_id")
        title = get_object_or_404(Title.objects, pk=title_id)
        review = get_object_or_404(Review.objects, pk=review_id)
        queryset = Comment.objects.filter(title=title, review=review).all()
        return queryset

    def perform_create(self, serializer):
        """Create a new comment."""
        title_id = self.kwargs.get("title_id")
        review_id = self.kwargs.get("review_id")
        title = get_object_or_404(Title.objects, pk=title_id)
        review = get_object_or_404(Review.objects, pk=review_id)
        serializer.save(author=self.request.user, title=title,
                        review=review)
