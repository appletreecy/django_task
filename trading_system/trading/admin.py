from django.contrib import admin
from .models import Stock, Trade

# Register the Stock model


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')

# Register the Trade model


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'stock', 'quantity',
                    'trade_type', 'timestamp')
