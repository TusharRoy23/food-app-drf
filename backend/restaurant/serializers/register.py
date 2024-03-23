from rest_framework import serializers

from ..models import Restaurant


class RegisterRestaurantSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)

    class Meta:
        model = Restaurant
        exclude = ["code", "status"]
