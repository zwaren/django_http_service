from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.utils import timezone
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from .exceptions import CityDoesntExistException, StreetDoesntExistException
from .models import City, Shop, Street
from .serializers import CitySerializer, ShopSerializer, StreetSerializer


class CityList(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetList(ListAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

    def get_queryset(self):
        streets = self.queryset

        city_id = self.request.GET.get('city_id')
        if city_id:
            try:
                City.objects.get(id=city_id)
            except ObjectDoesNotExist:
                raise CityDoesntExistException()
            streets = streets.filter(city=city_id)

        return streets


class ShopList(ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_queryset(self):
        shops = self.queryset

        street_name = self.request.GET.get('street')
        if street_name:
            try:
                Street.objects.get(name=street_name)
            except ObjectDoesNotExist:
                raise StreetDoesntExistException()
            shops = shops.filter(street__name=street_name)

        city_name = self.request.GET.get('city')
        if city_name:
            try:
                City.objects.get(name=city_name)
            except ObjectDoesNotExist:
                raise CityDoesntExistException()
            shops = shops.filter(city__name=city_name)

        is_open = self.request.GET.get('open')
        nowtime = timezone.now().time()
        if is_open == '1':
            shops = shops.filter(Q(open_time__lte=nowtime) & Q(close_time__gte=nowtime))
        elif is_open == '0':
            shops = shops.filter(Q(open_time__gt=nowtime) | Q(close_time__lt=nowtime))

        return shops
