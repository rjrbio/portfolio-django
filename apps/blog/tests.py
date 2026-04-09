from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post


class PostListAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Post.objects.create(title="Post Uno", excerpt="Extracto 1", content="Contenido 1", published=True)
        Post.objects.create(title="Post Dos", excerpt="Extracto 2", content="Contenido 2", published=True)
        Post.objects.create(title="Borrador", excerpt="Extracto 3", content="Contenido 3", published=False)

    def test_list_returns_200(self):
        response = self.client.get('/api/v1/blog/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_has_pagination_envelope(self):
        response = self.client.get('/api/v1/blog/')
        self.assertIn('count', response.data)
        self.assertIn('results', response.data)

    def test_list_excludes_unpublished(self):
        response = self.client.get('/api/v1/blog/')
        self.assertEqual(response.data['count'], 2)

    def test_detail_returns_200(self):
        response = self.client.get('/api/v1/blog/post-uno/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_not_found_returns_404(self):
        response = self.client.get('/api/v1/blog/no-existe/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_detail_unpublished_returns_404(self):
        response = self.client.get('/api/v1/blog/borrador/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

