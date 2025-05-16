from django.urls import path
from . import views

urlpatterns = [
    path('movies/<int:year>/<str:query>/', views.get_movie_query, name='movie_query'),
    path('movies/', views.get_movie_year, name='movie_list'),
]