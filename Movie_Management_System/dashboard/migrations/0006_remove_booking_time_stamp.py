# Generated by Django 3.1.7 on 2021-03-27 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210325_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='time_stamp',
        ),
    ]
