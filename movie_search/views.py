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
def get_movie_details(request):
    page = request.GET.get('page', 1)  # クエリパラメータからページ番号を取得
    year = request.GET.get('year', 2024) # 検索用のリリース年
    query = request.GET.get('query', '') # 検索キーワード
    
    # 検索クエリがある場合はsearch/movieエンドポイントを使用
    if query:
        url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=ja-JP&page={page}&query={query}'
        response = requests.get(url)
        data = response.json()
        
        # 検索結果を年でフィルタリング
        filtered_results = [
            movie for movie in data.get('results', [])
            if movie.get('release_date', '').startswith(str(year))
        ]
        
        # フィルタリング後の結果を新しいレスポンスとして返す
        return Response({
            'page': data.get('page', 1),
            'results': filtered_results,
            'total_results': len(filtered_results),
            'total_pages': data.get('total_pages', 1)
        })
    else:
        # 検索クエリがない場合は通常のdiscover/movieエンドポイントを使用
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&language=ja-JP&page={page}&primary_release_date.gte={year}-01-01&primary_release_date.lte={year}-12-31'
        response = requests.get(url)
        return Response(response.json())
