from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import generics



        

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
        fields = '__all__'
        model = Title            

