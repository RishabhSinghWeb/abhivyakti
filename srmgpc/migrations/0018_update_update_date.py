# Generated by Django 3.0.8 on 2020-12-19 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srmgpc', '0017_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
    ]
