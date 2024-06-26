from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from .models import Stock, Trade
from .serializers import StockSerializer, TradeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]


class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically sets the user field to the logged-in user
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='total_value', url_name='total_value')
    def total_value(self, request):
        user = request.user
        stock_id = request.query_params.get('stock_id')
        stock = get_object_or_404(Stock, id=stock_id)
        trades = Trade.objects.filter(user=user, stock=stock)
        total_value = sum(trade.order_value() for trade in trades)
        return Response({'total_value': total_value})
