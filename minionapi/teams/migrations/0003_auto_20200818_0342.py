# Generated by Django 2.2.15 on 2020-08-18 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20200818_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='phone1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='phone2',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
