from django.urls import path

from . import views

urlpatterns = [
    path('city/street', views.StreetList.as_view()),
    path('city', views.CityList.as_view()),
    path('shop', views.ShopList.as_view()),
]
