# Generated by Django 3.1.6 on 2021-05-14 05:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210513_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelphoto',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_photos', to='api.hotel', verbose_name='Hotel'),
        ),
        migrations.AlterField(
            model_name='hotelphoto',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='hotel_photos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])]),
        ),
    ]
