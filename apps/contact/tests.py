from django.test import TestCase, override_settings
from rest_framework.test import APIClient
from rest_framework import status


VALID_PAYLOAD = {
    'name': 'Juan Pérez',
    'email': 'juan@example.com',
    'subject': 'Consulta de prueba',
    'message': 'Este es un mensaje válido sin enlaces externos.',
}


# DummyCache evita que el throttle acumule entre tests
@override_settings(CACHES={'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}})
class ContactAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/v1/contact/'

    def test_valid_message_returns_201(self):
        response = self.client.post(self.url, VALID_PAYLOAD, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_missing_fields_returns_400(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_message_with_url_returns_400(self):
        payload = {**VALID_PAYLOAD, 'message': 'Visita https://spam.com para más info'}
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_message_with_www_returns_400(self):
        payload = {**VALID_PAYLOAD, 'message': 'Ve a www.spam.com para más detalles sobre el tema'}
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_message_too_short_returns_400(self):
        payload = {**VALID_PAYLOAD, 'message': 'Corto'}
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_name_too_short_returns_400(self):
        payload = {**VALID_PAYLOAD, 'name': 'J'}
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_email_returns_400(self):
        payload = {**VALID_PAYLOAD, 'email': 'noesunemail'}
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

