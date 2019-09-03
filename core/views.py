from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import City, Shop, Street


@api_view(['GET'])
def city_list(request): pass

@api_view(['GET'])
def street_list(request): pass

@api_view(['GET'])
def shop_list(request): pass