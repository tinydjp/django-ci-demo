import pytest
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


# Create your tests here.
@pytest.mark.django_db
class TestCompany(APITestCase):
    url = reverse('list-product')

    def test_list_company(self):
        response = self.client.get(self.url, format='json')
        assert response.status_code == status.HTTP_200_OK
