# Generated by Django 3.0.8 on 2020-12-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srmgpc', '0006_auto_20201114_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='college',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
