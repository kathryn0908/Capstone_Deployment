from django.contrib import admin
from .models import Restaurant, Trending, User, Review, Favorite, StarRating
from django.contrib.auth.admin import UserAdmin


admin.site.register(Restaurant)
admin.site.register(Trending)
admin.site.register(User, UserAdmin)
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(StarRating)
