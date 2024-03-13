from rest_framework.test import APITestCase
from core.account.models import CustomUser
from django.contrib.auth import authenticate
from rest_framework import status
from django.urls import reverse

class AccountTestCase(APITestCase):
    """Testcases for the account endpoints."""

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            first_name="first",
            last_name="last",
            email="use1@gmail.com",
            password="password01",
            is_admin=False)

    def test_register_user(self):
        """Tests the register user endpoint."""
        payload = {
            "first_name":"first",
            "last_name":"last",
            "email":"user@gmail.com",
            "password":"password01",
            "password2":"password01"}
        response = self.client.post(reverse('register'), payload)
        assert(response.status_code == status.HTTP_200_OK)
       
    def test_user_login(self):
        """Tests the login user endpoint."""
        payload = {
            "email":"user1@gmail.com",
            "password":"password01",
        }
        response = self.client.post(reverse('login'), payload)
        assert(response.status_code == status.HTTP_200_OK)
       
    def test_user_login_invalid(self):
        """Tests the login user endpoint with invalid credentials."""
        payload = {
            "email":"user1@gmail.com",
            "password":"password02",
        }
        response = self.client.post(reverse('login'), payload)
        assert(response.data['status'] == status.HTTP_404_NOT_FOUND)

        