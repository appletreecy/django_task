from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StockViewSet, TradeViewSet

router = DefaultRouter()
router.register(r'stocks', StockViewSet)
router.register(r'trades', TradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
