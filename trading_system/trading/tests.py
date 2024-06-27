from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from trading.models import Stock, Trade


class TradingSystemTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        # Create a test stock
        self.stock = Stock.objects.create(name='TestStock', price=100.00)

    def test_place_trade(self):
        url = reverse('trade-list')
        print(f"trade-list url is{url}")
        data = {
            'stock': self.stock.id,
            'quantity': 10,
            'trade_type': 'BUY'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['quantity'], 10)
        self.assertEqual(response.data['trade_type'], 'BUY')

    def test_total_value(self):
        Trade.objects.create(user=self.user, stock=self.stock,
                             quantity=10, trade_type='BUY')
        Trade.objects.create(user=self.user, stock=self.stock,
                             quantity=5, trade_type='BUY')
        url = reverse('trade-total_value')
        print(f'url is {url}')
        response = self.client.get(url, {'stock_id': self.stock.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_value'], 1500.00)
