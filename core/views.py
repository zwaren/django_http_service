import datetime

from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City, Shop, Street
from .serializers import CitySerializer, ShopSerializer, StreetSerializer


class CityList(APIView):
    def get(self, request, format=None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


class StreetList(APIView):
    def get(self, request, format=None):
        streets = Street.objects.all()
        city_id = request.GET.get('city_id')
        if city_id:
            streets = streets.filter(city=city_id)
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)


class ShopList(APIView):
    def get(self, request, format=None):
        shops = Shop.objects.all()

        street_name = request.GET.get('street')
        if street_name:
            shops = shops.filter(street__name=street_name)

        city_name = request.GET.get('city')
        if city_name:
            shops = shops.filter(city__name=city_name)

        is_open = request.GET.get('open')
        nowtime = datetime.datetime.now().time()
        if is_open == '1':
            shops = shops.filter(Q(open_time__lte=nowtime) & Q(close_time__gte=nowtime))
        elif is_open == '0':
            shops = shops.filter(Q(open_time__gt=nowtime) | Q(close_time__lt=nowtime))

        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
