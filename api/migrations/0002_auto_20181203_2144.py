# Generated by Django 2.1.3 on 2018-12-03 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='guest_id',
            field=models.CharField(default=42, max_length=200),
            preserve_default=False,
        ),
    ]
