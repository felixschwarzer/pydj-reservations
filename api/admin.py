from django.contrib import admin
from django.contrib import admin
from .models import Reservation, ReservationLog

# Register your models here.
admin.site.register(Reservation)
admin.site.register(ReservationLog)
