from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_mysql.models import EnumField

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


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length = 20)

    def __str__(self):
        return self.name


class Cinema(models.Model):
    name = models.CharField(max_length=100)
    total_cinema_halls = models.IntegerField()
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    total_seats = models.IntegerField()
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CinemaSeat(models.Model):
    seat_number = models.IntegerField()
    type = EnumField(choices=['Basic', 'Executive', 'Premium', 'VIP'])
    cinemal_hall_id = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)


"""
class Show(models.Model):
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
"""
