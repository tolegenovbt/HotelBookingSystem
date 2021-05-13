# Generated by Django 3.1.6 on 2021-05-13 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210513_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_reservations', to='api.hotel', verbose_name='Hotel'),
        ),
    ]