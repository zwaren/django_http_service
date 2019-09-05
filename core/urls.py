from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('city/street', views.StreetList.as_view()),
    path('city', views.CityList.as_view()),
    path('shop', views.ShopList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)