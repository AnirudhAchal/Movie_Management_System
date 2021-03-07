from django.shortcuts import render
from .models import Movie

# Create your views here.
def home(request):
    context = {
        'movies': Movie.objects.all()
    }
    return render(request, 'dashboard/home.html', context)


def about(request):
    return render(request, 'dashboard/about.html', {'title': 'About Page'})
