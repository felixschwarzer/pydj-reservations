# Generated by Django 2.1.3 on 2018-12-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20181204_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='x',
            field=models.FloatField(default='0.00'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='y',
            field=models.FloatField(default='0.00'),
        ),
    ]
