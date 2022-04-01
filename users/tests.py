from django.test import TestCase
from django.contrib .auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.

CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    """Test the users Api (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """test creating user with a valid payload is succesful"""
        payload = {
            'email' : 'test@gmail.com',
            'password' : 'testpass',
            'name' : 'testname',
        }

        res = self.client.post(CREATE_USER_URL, payload)
