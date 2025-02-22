from rest_framework import serializers

from ..models import Store


class RegisterStoreSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)

    class Meta:
        model = Store
        exclude = ["code", "status"]
