# Generated by Django 3.1.6 on 2021-05-15 03:46

import api.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210515_0715'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='room',
            managers=[
                ('objects', api.models.RoomManager()),
            ],
        ),
    ]
