# Generated by Django 3.1.6 on 2021-05-13 11:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210513_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomphoto',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='room_photos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])]),
        ),
    ]
