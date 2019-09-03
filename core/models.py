from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200)


class Street(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Shop(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.CharField(max_length=200)
    open_time = models.TimeField()
    close_time = models.TimeField()