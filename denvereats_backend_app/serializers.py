from rest_framework import serializers
from . import models
# from django.contrib.auth.hashers import make_password

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        
        fields = ('id','thumb', 'name', 'cuisines', 'timings', 'url', 'address', 'phone_number', 'has_online_delivery', 'is_delivering_now', 'average_cost_for_two', 'highlights', 'favorites', 'reviews', 'images')
        depth = 3

class TrendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Trending 
        fields = ('id', 'image_url', 'url', 'title', 'description') 