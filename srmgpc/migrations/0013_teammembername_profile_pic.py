# Generated by Django 3.0.8 on 2020-12-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srmgpc', '0012_auto_20201214_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammembername',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to='team-profile'),
        ),
    ]
