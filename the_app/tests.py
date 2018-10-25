from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class ViewsTestCases(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_home_returns_message(self):
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['message'], 'successful')

