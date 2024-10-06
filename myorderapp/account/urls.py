from django.urls import path, include
from .views import login,register

urlpatterns = [
    path('signup/',register,name='signup'),
    path('login/',login,name='login'),
     path('api-auth/',include('rest_framework.urls')),
]
