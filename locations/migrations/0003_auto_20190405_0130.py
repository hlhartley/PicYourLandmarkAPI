# Generated by Django 2.2 on 2019-04-05 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20190404_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locations',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='locations',
            old_name='longitude',
            new_name='lon',
        ),
    ]