from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_movie_details, name='movie_list'),
    path('movies/<int:year>/', views.get_movie_year, name='movie_year'),
    path('movies/<int:year>/<str:query>/', views.get_movie_query, name='movie_query'),
]