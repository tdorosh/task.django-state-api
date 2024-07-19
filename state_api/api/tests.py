from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from states.models import State


class RandomStateAPIViewTests(APITestCase):

    def setUp(self):
        State.objects.create(
            name='Ukraine',
            capital='Kyiv',
            area='603628.00',
            population=38000000,
        )

    def test_get_random_state(self):
        """Ensure api returns random state."""
        url = reverse('random-state')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Ukraine')
        self.assertEqual(response.data['capital'], 'Kyiv')
        self.assertEqual(response.data['area'], '603628.00')
        self.assertEqual(response.data['population'], 38000000)
