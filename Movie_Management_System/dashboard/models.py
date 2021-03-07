from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=20)
    release_date = models.DateTimeField(default=timezone.now)
    genre = models.CharField(max_length=20)
    pg_rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.IntegerField()

    def __str__(self):
        return self.title
