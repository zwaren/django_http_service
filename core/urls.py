from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    path('city/street', views.StreetList.as_view()),
    path('city', views.CityList.as_view()),
    path('shop', views.ShopList.as_view()),
    path('register', views.Registration.as_view()),
    path('login', obtain_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
