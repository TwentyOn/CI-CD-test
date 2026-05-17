from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .views import TestView


# Create your tests here.
class TestTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_test_view(self):
        url = reverse('test')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'success')
