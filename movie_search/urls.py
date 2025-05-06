from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_movie_details, name='movie_details'),
]