# Generated by Django 2.1.3 on 2018-12-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20181204_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
