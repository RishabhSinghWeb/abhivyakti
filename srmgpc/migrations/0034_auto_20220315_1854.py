# Generated by Django 3.0.8 on 2022-03-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srmgpc', '0033_auto_20201230_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='team',
            field=models.CharField(blank=True, default='NA', max_length=200, null=True),
        ),
    ]
