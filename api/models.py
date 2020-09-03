<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
=======
from django.core.validators import MaxValueValidator, MinValueValidator
>>>>>>> master
from django.db import models
from django.contrib.auth.models import AbstractUser

<<<<<<< HEAD
#User = get_user_model()
=======
>>>>>>> master

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=25, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

<<<<<<< HEAD

User = get_user_model()
=======
    class Meta:
        ordering = ('username', )
>>>>>>> master


class Genre(models.Model):
    name = models.TextField(unique=True)
    slug = models.SlugField(max_length=200, unique=True, )

    def __str__(self):
        return f"{self.name, self.slug}"

    class Meta:
        ordering = ('-pk', )


class Category(models.Model):
    name = models.TextField(unique=True)
    slug = models.SlugField(max_length=200, unique=True, )

    def __str__(self):
        return f"{self.name, self.slug}"

    class Meta:
        ordering = ('-pk', )


class Title(models.Model):
    name = models.TextField('Название', )
    year = models.IntegerField('Год выпуска', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField('Genre', related_name="genres", blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 related_name="categories", blank=True, null=True)

    class Meta:
        ordering = ('-pk', )


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name="reviews", null=False)
    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                               related_name="reviews", null=False)
    score = models.PositiveIntegerField("Оценка", null=False,
                                        validators=[MinValueValidator(1),
                                                    MaxValueValidator(10)])
    pub_date = models.DateTimeField("Дата публикации",
                                    auto_now_add=True)

    class Meta:
        ordering = ('-pub_date', )


class Comment(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name="comments", null=False)
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name="comments", null=False)
    text = models.TextField(null=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                               related_name="comments", null=False)
    pub_date = models.DateTimeField("Дата публикации",
                                    auto_now_add=True)
<<<<<<< HEAD
=======

    class Meta:
        ordering = ('-pub_date', )
>>>>>>> master
