from django.conf import settings
from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='topics',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='posts',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.message[:50]