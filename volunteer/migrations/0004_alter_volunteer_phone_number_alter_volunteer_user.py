# Generated by Django 4.0.3 on 2022-05-04 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('volunteer', '0003_volunteer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+77779185334', max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer', to=settings.AUTH_USER_MODEL),
        ),
    ]
