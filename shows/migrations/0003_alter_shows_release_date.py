# Generated by Django 3.2.6 on 2021-08-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_shows_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='release_date',
            field=models.DateField(verbose_name='%d-%m-%Y'),
        ),
    ]
