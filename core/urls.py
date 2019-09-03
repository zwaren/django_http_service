from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('city/', views.city_list),
    path('city/street/', views.street_list),
    path('shop/', views.shop_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)