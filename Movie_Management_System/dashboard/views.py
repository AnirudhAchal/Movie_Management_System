from django.shortcuts import render
from django.views.generic import DetailView
from .models import Movie

# Create your views here.
def home(request):
    if request.method == 'GET':

        # Get language
        if len(request.GET.getlist('language')) == 0: # No language selected
            LANGUAGES = "(SELECT language FROM dashboard_movie)"

        else:
            LANGUAGES = request.GET.getlist('language').__str__().replace('[', '(').replace(']', ')')

        # Get genre
        if len(request.GET.getlist('genre')) == 0: # No genre selected
            GENRES = "(SELECT genre FROM dashboard_movie)"

        else:
            GENRES = request.GET.getlist('genre').__str__().replace('[', '(').replace(']', ')')

        # Get max duration
        if request.GET.get('duration'):
            DURATION = request.GET.get('duration')
        else:
            DURATION = "(SELECT MAX(duration) FROM dashboard_movie)"

        # Get max pg_rating
        if request.GET.get('pg_rating'):
            PG_RATING = request.GET.get('pg_rating')
        else:
            PG_RATING = "(SELECT MAX(pg_rating) FROM dashboard_movie)"

        # Get order_by
        if request.GET.get('order_by'):
            ORDER_BY = request.GET.get('order_by')
        else:
            ORDER_BY = "release_date"

        # Get desc
        if request.GET.get('desc'):
            DESC = "DESC"
        else:
            DESC = ""

    languages_query = f'SELECT DISTINCT 1 as id, language FROM dashboard_movie'
    genres_query = f'SELECT DISTINCT 1 as id, genre FROM dashboard_movie'
    pg_ratings_query = f'SELECT DISTINCT 1 as id, pg_rating FROM dashboard_movie ORDER BY pg_rating'
    movies_query = f"""
                        SELECT * FROM dashboard_movie
                        WHERE language IN {LANGUAGES}
                        AND genre in {GENRES}
                        AND duration <= {DURATION}
                        AND pg_rating <= {PG_RATING}
                        ORDER BY {ORDER_BY}
                        {DESC}
                    """

    print(movies_query)
    context = {
        # 'movies': Movie.objects.all()
        'movies': Movie.objects.raw(movies_query),
        'languages': Movie.objects.raw(languages_query),
        'genres': Movie.objects.raw(genres_query),
        'pg_ratings': Movie.objects.raw(pg_ratings_query)
    }

    return render(request, 'dashboard/home.html', context)


def about(request):
    return render(request, 'dashboard/about.html', {'title': 'About Page'})


class MovieDetailView(DetailView):
    model = Movie

def search_bar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        movie = Movie.objects.all().filter(title = search)
        return render(request,'dashboard/search_bar.html',{'searched_movie': movie})