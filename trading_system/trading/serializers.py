from rest_framework import serializers
from .models import Stock, Trade


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class TradeSerializer(serializers.ModelSerializer):
    order_value = serializers.ReadOnlyField()

    class Meta:
        model = Trade
        fields = '__all__'
        read_only_fields = ('user',)
