from django.contrib import admin
from .models import Movie
from .models import City
from .models import Cinema
from .models import CinemaHall
from .models import CinemaSeat
from .models import Show
from .models import Booking
from .models import ShowSeat

# Register your models here.
admin.site.register(Movie)
admin.site.register(City)
admin.site.register(Cinema)
admin.site.register(CinemaHall)
admin.site.register(CinemaSeat)
admin.site.register(Show)
admin.site.register(Booking)
admin.site.register(ShowSeat)
