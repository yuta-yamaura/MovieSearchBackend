from django.urls import path
from . import views

urlpatterns = [
    path('movies/<int:movie_id>/', views.get_movie_details, name='movie_details'),
]