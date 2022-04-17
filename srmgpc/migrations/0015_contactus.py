# Generated by Django 3.0.8 on 2020-12-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srmgpc', '0014_auto_20201216_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30, null=True)),
                ('last_name', models.CharField(default='', max_length=30, null=True)),
                ('email', models.EmailField(default='', max_length=30, null=True)),
                ('phone', models.CharField(default='', max_length=30, null=True)),
                ('message', models.CharField(default='', max_length=500, null=True)),
            ],
        ),
    ]
