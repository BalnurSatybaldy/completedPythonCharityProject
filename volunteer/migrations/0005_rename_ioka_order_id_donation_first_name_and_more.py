# Generated by Django 4.0.3 on 2022-05-04 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0004_alter_volunteer_phone_number_alter_volunteer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='ioka_order_id',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='username',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='user',
        ),
    ]
