from django.conf import settings
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    board = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')
    #board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comments')
    #author
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_edit_url(self):
        return reverse('comment_edit', args=[self.board.pk, self.pk])