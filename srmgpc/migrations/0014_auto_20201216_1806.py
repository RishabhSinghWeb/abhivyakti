# Generated by Django 3.0.8 on 2020-12-16 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srmgpc', '0013_teammembername_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembername',
            name='branch',
            field=models.CharField(blank=True, choices=[('EE', 'EE'), ('ECE', 'ECE'), ('CSE', 'CSE'), ('IT', 'IT'), ('ME', 'ME'), ('CE', 'CE'), ('BBA', 'BBA'), ('BCA', 'BCA'), ('MBA', 'MBA')], max_length=100),
        ),
        migrations.AlterField(
            model_name='teammembername',
            name='year',
            field=models.CharField(blank=True, choices=[('1st year', '1st year'), ('2nd year', '2nd year'), ('3rd year', '3rd year'), ('4th year', '4th year')], max_length=100),
        ),
    ]
