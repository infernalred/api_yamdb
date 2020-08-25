from django.db import models


                        


class Genre(models.Model):
    name = models.TextField(unique=True)
    slug = models.SlugField(max_length=200, unique=True, )

    def __str__(self):   
        return f"{self.name, self.slug}"


class Category(models.Model):
    name = models.TextField(unique=True)
    slug = models.SlugField(max_length=200, unique=True, )

    def __str__(self):   
        return f"{self.name, self.slug}"

class Title(models.Model):
    name = models.TextField('Название', )
    year = models.IntegerField('Год выпуска', )
    description = models.TextField()
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, 
                               related_name="genres")
    #rating = models.IntegerField('Рейтинг', )
    category = models.ForeignKey('Category', on_delete=models.CASCADE, 
                               related_name="categories")          