# Generated by Django 3.1.6 on 2021-05-14 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210514_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='number_of_stars',
            new_name='rating',
        ),
    ]