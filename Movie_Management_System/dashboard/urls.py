from django.urls import path
from .views import MovieDetailView

from . import views


urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('about/', views.about, name='dashboard-about')
]
