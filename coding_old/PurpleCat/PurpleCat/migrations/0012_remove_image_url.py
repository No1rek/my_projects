# Generated by Django 2.0.3 on 2018-03-24 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PurpleCat', '0011_auto_20180324_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
    ]
