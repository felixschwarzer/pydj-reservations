from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# api/models.py
class Reservation(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    seat = models.IntegerField(
        default='1'
    )
    secret = models.CharField(
        max_length=200
    )
    x = models.FloatField(
        default='0.1',
    )
    y = models.FloatField(
        default='0.1',
    )
    note = models.TextField(
        blank=True
    )
    date = models.CharField(
        max_length=200
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return '%s %s %s ' % (self.seat, self.secret, self.note)

class ReservationLog(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    res_id = models.IntegerField(
        default='0'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    creation_date = models.DateTimeField(
        default = timezone.now
    )
    updated_by = models.ForeignKey(
        User,
        related_name="updated_by",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    res_creator = models.ForeignKey(
        User,
        related_name="res_creator",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    seat = models.IntegerField(
        default='1'
    )
    secret = models.CharField(
        max_length=200
    )
    x = models.FloatField(
        default='0.1',
    )
    y = models.FloatField(
        default='0.1',
    )
    note = models.TextField(
        blank=True
    )
    date = models.CharField(
        max_length=200
    )
