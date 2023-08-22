from django.test import TestCase
from django.urls import reverse

class WeatherViewTest(TestCase):

    def test_valid_city(self):
        response = self.client.get(reverse('weather_view', kwargs={'city': 'San Francisco'}))  # Change this line
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'temperature': 14, 'weather': 'Cloudy'})

    def test_invalid_city(self):
        response = self.client.get(reverse('weather_view', kwargs={'city': 'InvalidCity'}))  # Change this line
        self.assertEqual(response.status_code, 404)
