# Generated by Django 3.1.6 on 2021-05-15 03:53

import api.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210515_0946'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('objects', api.models.CommentManager()),
            ],
        ),
    ]
