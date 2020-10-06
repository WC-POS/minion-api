# Generated by Django 2.2.15 on 2020-09-19 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0005_auto_20200823_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.PositiveIntegerField(verbose_name='Company ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='Company Name')),
                ('client_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Client Name')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('description', models.TextField()),
                ('summary', models.TextField()),
                ('resolved', models.BooleanField(default=True)),
                ('followup', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_entries', related_query_name='work_entry', to='teams.Team')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='work_entries', related_query_name='work_entry', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Work Entry',
                'verbose_name_plural': 'Work Entries',
            },
        ),
    ]