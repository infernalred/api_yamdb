from django.contrib.auth import get_user_model, AbstractUser
from django.db import models

User = get_user_model()


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=25, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)


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
    genre = models.ManyToManyField('Genre', related_name="genres")
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 related_name="categories")


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
