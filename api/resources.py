# api/resources.py

from tastypie.resources import ModelResource
from api.models import Reservation
from tastypie.authorization import Authorization
class ReservationResource(ModelResource):
    class Meta:
        queryset = Reservation.objects.all()
        resource_name = 'reservation'
        authorization = Authorization()
        #fields = ['title', 'body']
