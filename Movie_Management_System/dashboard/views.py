from django.shortcuts import render
from .models import Movie

# Create your views here.
def home(request):
    if request.method == 'GET':
        if len(request.GET.getlist('language')) == 0 or 'other' in request.GET.getlist('language'):
            LANGUAGES = "(SELECT language FROM dashboard_movie)"

        else:
            LANGUAGES = request.GET.getlist('language').__str__().replace('[', '(').replace(']', ')')

    movie_query = f'SELECT * FROM dashboard_movie WHERE language IN {LANGUAGES}'

    context = {
        # 'movies': Movie.objects.all()
        'movies': Movie.objects.raw(movie_query)
    }

    return render(request, 'dashboard/home.html', context)


def about(request):
    return render(request, 'dashboard/about.html', {'title': 'About Page'})
