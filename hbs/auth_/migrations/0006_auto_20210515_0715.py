# Generated by Django 3.1.6 on 2021-05-15 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0005_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='Phone Number'),
        ),
    ]
