from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


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
    # rating = models.IntegerField('Рейтинг', )
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 related_name="categories")


# class Rating(models.Model):
#     pass


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name="reviews", null=False)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="reviews", null=False)
    score = models.PositiveIntegerField("Оценка", null=False)
    pub_date = models.DateTimeField("Дата публикации",
                                    auto_now_add=True)


class Comment(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name="comments", null=False)
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name="comments", null=False)
    text = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="comments", null=False)
    pub_date = models.DateTimeField("Дата публикации",
                                    auto_now_add=True)
