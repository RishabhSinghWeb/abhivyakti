# Generated by Django 3.0.8 on 2020-12-30 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srmgpc', '0031_registration_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventname',
            name='event_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]