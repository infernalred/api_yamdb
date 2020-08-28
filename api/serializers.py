from rest_framework import serializers

from .models import Comment, Review, Title, Category, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "slug")
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "slug")
        model = Category


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    category = CategorySerializer()

    class Meta:
        fields = ("id", "name", "year", "genre", "category", "description")
        read_only_fields = ("id", )
        model = Title


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "slug")
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "slug")
        model = Category


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer()

    class Meta:
        fields = ("id", "name", "year", "genre", "category", "description")
        read_only_fields = ("id", )
        model = Title

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username",
                                          read_only=True)

    class Meta:
        fields = ("id", "text", "author", "score", "pub_date",)
        read_only_fields = ("id", "author", "pub_date")
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username",
                                          read_only=True)

    class Meta:
        fields = ("id", "text", "author", "pub_date",)
        read_only_fields = ("id", "author", "pub_date",)
        model = Comment