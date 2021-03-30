from django.urls import path, include
from .views import MovieDetailView
from . import views


urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('my_bookings/', views.my_bookings, name='dashboard-my_bookings'),
    path('search_bar/',views.search_bar,name = "search_bar"),
    path('movie/<int:pk>/book', views.book, name='movie-booking'),
]
