# Generated by Django 2.2.15 on 2020-08-23 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='cw_private',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='cw_public',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
