from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name="reviews")
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="reviews")
    score = models.PositiveIntegerField()
    pub_date = models.DateTimeField("Дата публикации",
                                    auto_now_add=True)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name="comments")
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="comments")
    pub_date = models.DateTimeField("Дата публикации1",
                                    auto_now_add=True)
