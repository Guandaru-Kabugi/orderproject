from django.urls import path,include
from .views import OrderViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'orders',OrderViewSet,basename='Order')
urlpatterns = [
    path('',include(router.urls)),
]