# Generated by Django 2.1.3 on 2018-12-04 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181204_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='x',
            field=models.DecimalField(decimal_places=2, default='0.0', max_digits=4),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='y',
            field=models.DecimalField(decimal_places=2, default='0.0', max_digits=4),
        ),
    ]
