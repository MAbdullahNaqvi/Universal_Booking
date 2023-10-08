# Generated by Django 4.2.5 on 2023-10-07 18:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolarTrips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planets',
            name='passengers',
            field=models.ManyToManyField(related_name='packages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planets',
            name='wishlist',
            field=models.ManyToManyField(related_name='wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]