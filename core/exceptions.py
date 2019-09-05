from rest_framework.exceptions import APIException


class CityDoesntExistException(APIException):
    status_code = 400
    default_detail = "City doesn't found"


class StreetDoesntExistException(APIException):
    status_code = 400
    default_detail = "Street doesn't found"
