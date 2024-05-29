from django.urls import path
from .views import restaurant_detail

urlpatterns = [
    path('restaurant/<int:restaurant_id>/', restaurant_detail, name='restaurant_detail'),
]
