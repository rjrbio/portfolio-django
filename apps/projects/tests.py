from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Project


class ProjectListAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Project.objects.create(
            title="Proyecto Uno", description="Desc 1", technologies="Django, Vue"
        )
        Project.objects.create(
            title="Proyecto Dos", description="Desc 2", technologies="React, Node"
        )

    def test_list_returns_200(self):
        response = self.client.get('/api/v1/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_has_pagination_envelope(self):
        response = self.client.get('/api/v1/projects/')
        self.assertIn('count', response.data)
        self.assertIn('results', response.data)

    def test_list_count(self):
        response = self.client.get('/api/v1/projects/')
        self.assertEqual(response.data['count'], 2)

    def test_detail_returns_200(self):
        response = self.client.get('/api/v1/projects/proyecto-uno/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_not_found_returns_404(self):
        response = self.client.get('/api/v1/projects/no-existe/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

