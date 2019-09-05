from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import City, Shop, Street


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, 
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], 
            validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
