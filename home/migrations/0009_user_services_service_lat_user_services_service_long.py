# Generated by Django 4.0.3 on 2022-05-31 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_user_services_service_lat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_services',
            name='service_lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='user_services',
            name='service_long',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]