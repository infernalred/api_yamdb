from rest_framework import serializers

from .models import Comment, Review, Title, Category, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    category = CategorySerializer()

    class Meta:
        fields = ('name', 'year', 'genre', 'category', 'description')
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username",
                                          read_only=True)

    class Meta:
        fields = ("id", "text", "author", "score", "pub_date",)
        read_only_fields = ("id", "author", "pub_date")
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(slug_field="title",
                                         read_only=True)
    review = serializers.SlugRelatedField(slug_field="review",
                                          read_only=True)
    author = serializers.SlugRelatedField(slug_field="username",
                                          read_only=True)

    class Meta:
        fields = ("id", "text", "author", "pub_date",)
        read_only_fields = ("id", "author", "pub_date",)
        model = Comment
