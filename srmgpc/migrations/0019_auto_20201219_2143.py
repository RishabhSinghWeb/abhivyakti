# Generated by Django 3.0.8 on 2020-12-19 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srmgpc', '0018_update_update_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventresult',
            name='cell',
        ),
        migrations.RemoveField(
            model_name='eventresult',
            name='place',
        ),
        migrations.RemoveField(
            model_name='eventresult',
            name='winner_position',
        ),
    ]
