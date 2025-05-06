from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
import requests
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import environ
# Create your views here.

env = environ.Env()
env.read_env('.env')
TMDB_API_KEY = env('TMDB_API_KEY')

@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def getRoutes(request):
    routes = [
        'api/products/',
        'api/products/create',
        'api/products/upload',
        'api/products/<id>/reviews',
        'api/products/top/',
        'api/products/<id>/reviews',
        'api/products/delete/<id>',
        'api/products/<id>/reviews',
        'api/products/update/<id>',
        'api/products/<id>/reviews',
        'api/products/delete/<id>',
        'api/products/<id>/reviews',
        'api/products/delete/<id>',
    ]
    return Response(routes)

@api_view(['GET'])
def get_movie_details(request, movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}'
    print(url)
    response = requests.get(url)
    print(response)
    return Response(response.json())
