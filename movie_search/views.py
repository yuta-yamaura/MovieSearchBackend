from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from backend.settings import TMDB_API_KEY
from urllib.parse import unquote

# Create your views here.

@api_view(['GET'])
def get_movie_details(request):
    page = request.GET.get('page', 1)  # クエリパラメータからページ番号を取得
    year = request.GET.get('year', 2023) # 検索用のリリース年
    
    # 検索クエリがない場合は通常のdiscover/movieエンドポイントを使用
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&language=ja-JP&page={page}&primary_release_date.gte={year}-01-01&primary_release_date.lte={year}-12-31&sort_by=popularity.desc'
    response = requests.get(url)
    return Response(response.json())

@api_view(['GET'])
def get_movie_year(request, year):
    page = request.GET.get('page', 1)  # クエリパラメータからページ番号を取得
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&language=ja-JP&page={page}&primary_release_date.gte={year}-01-01&primary_release_date.lte={year}-12-31&sort_by=popularity.desc'
    response = requests.get(url)
    print(response.json())
    return Response(response.json())

@api_view(['GET'])
def get_movie_query(request, year, query):
    page = request.GET.get('page', 1)  # クエリパラメータからページ番号を取得
    # URLの文字化けを修正
    decoded_query = unquote(query)
    print(decoded_query)
    url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=ja-JP&query={decoded_query}&primary_release_year={year}&page={page}'
    response = requests.get(url)
    # print(response.json())
    return Response(response.json())
