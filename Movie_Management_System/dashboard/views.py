from django.shortcuts import render

# Dummy movies
posts = [
    {
        'director': 'Anirudh Achal',
        'title': 'My life',
        'description': 'This the description of the movie my life',
        'date_posted': 'January 19th, 2021'
    },
    {
        'director': 'Jk Rowling',
        'title': 'Harry Potter',
        'description': 'This the description of the movie harry potter',
        'date_posted': 'January 29th, 2021'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'dashboard/home.html', context)


def about(request):
    return render(request, 'dashboard/about.html')
