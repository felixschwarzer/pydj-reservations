# Generated by Django 2.1.3 on 2018-12-03 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('seat_number', models.IntegerField(default='1')),
                ('client_id', models.CharField(default='001', max_length=200)),
                ('block', models.IntegerField(default='1')),
                ('body', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('number', models.IntegerField(default='1', primary_key=True, serialize=False)),
                ('guest_id', models.CharField(blank=True, max_length=200, null=True)),
                ('note', models.TextField(blank=True)),
                ('taken', models.BooleanField(default=0)),
            ],
        ),
    ]
