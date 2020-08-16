from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Restaurant, Trending
from .serializers import RestaurantSerializer, TrendingSerializer


class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.AllowAny,)
    

    def __str__(self):
        return self.restaurant_text

class TrendingView(viewsets.ModelViewSet):
    queryset = Trending.objects.all()
    serializer_class = TrendingSerializer
    permission_classes = (permissions.AllowAny,)
    

    def __str__(self):
        return self.trending_text