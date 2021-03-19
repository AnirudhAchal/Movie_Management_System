from django.shortcuts import render
from .models import Movie

# Create your views here.
def home(request):
    if request.method == 'GET':

        # Get language
        if len(request.GET.getlist('language')) == 0: # No language selected
            LANGUAGES = "(SELECT language FROM dashboard_movie)"

        else:
            LANGUAGES = request.GET.getlist('language').__str__().replace('[', '(').replace(']', ')')

        if len(request.GET.getlist('genre')) == 0: # No genre selected
            GENRES = "(SELECT genre FROM dashboard_movie)"

        else:
            GENRES = request.GET.getlist('genre').__str__().replace('[', '(').replace(']', ')')


    movies_query = f'SELECT * FROM dashboard_movie WHERE language IN {LANGUAGES} AND genre in {GENRES}'
    languages_query = f'SELECT DISTINCT 1 as id, language FROM dashboard_movie'
    genres_query = f'SELECT DISTINCT 1 as id, genre FROM dashboard_movie'

    context = {
        # 'movies': Movie.objects.all()
        'movies': Movie.objects.raw(movies_query),
        'languages': Movie.objects.raw(languages_query),
        'genres': Movie.objects.raw(genres_query)
    }

    print(context['languages'])

    return render(request, 'dashboard/home.html', context)


def about(request):
    return render(request, 'dashboard/about.html', {'title': 'About Page'})
