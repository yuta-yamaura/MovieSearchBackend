from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.
class MovieViewsTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_movie_details_year_validation(self):
        """年数のバリデーションテスト"""
        # 2020年未満の年数が指定された場合
        response = self.client.get(reverse('movie_list'), {'year': 2019})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], '年数は2020年〜2024年で指定してください')

        # 2024年より大きい年数が指定された場合
        response = self.client.get(reverse('movie_list'), {'year': 2025})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], '年数は2020年〜2024年で指定してください')

        # 有効な年数が指定された場合
        response = self.client.get(reverse('movie_list'), {'year': 2023})
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', data)
        self.assertIn('page', data)
        self.assertIn('total_pages', data)
        self.assertIn('total_results', data)
        
        # 最初の映画データの構造を確認
        if data['results']:
            movie = data['results'][0]
            self.assertIn('title', movie)
            self.assertIn('release_date', movie)
            self.assertIn('overview', movie)
            self.assertIn('vote_average', movie)
            self.assertIn('poster_path', movie)