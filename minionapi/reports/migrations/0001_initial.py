# Generated by Django 2.2.15 on 2020-09-08 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255, verbose_name='Client Name')),
                ('company_id', models.PositiveIntegerField(verbose_name='Company ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='Company Name')),
                ('report_type', models.CharField(choices=[('CUSTOMER_SERVICE', 'Customer Service')], max_length=255)),
                ('draft', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reports', related_query_name='report', to=settings.AUTH_USER_MODEL)),
                ('last_edited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edited_reports', related_query_name='edited_report', to=settings.AUTH_USER_MODEL, verbose_name='Last Edited By')),
            ],
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=1024)),
                ('company', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TimeEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_records', related_query_name='time_record', to='reports.Report')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Time Entry',
                'verbose_name_plural': 'Time Entries',
            },
        ),
        migrations.CreateModel(
            name='InventoryCheckOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('serial', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_checkouts', related_query_name='inventory_checkout', to='reports.Report')),
            ],
            options={
                'verbose_name': 'Inventory Check Out',
                'verbose_name_plural': 'Inventory Check Outs',
            },
        ),
        migrations.CreateModel(
            name='CustomerService',
            fields=[
                ('report_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='reports.Report')),
                ('service_type', models.CharField(choices=[('INSTALL', 'Installation'), ('SALES', 'Sales'), ('SERVICE', 'Service Trip'), ('TRAINING', 'Training')], max_length=255, verbose_name='Service Type')),
                ('description', models.TextField()),
                ('billable', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('pictures', models.BooleanField(default=False)),
                ('reviewed', models.BooleanField(default=False)),
                ('satisfied', models.BooleanField(default=False)),
                ('tested', models.BooleanField(default=False)),
                ('summary', models.TextField()),
                ('signature', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_service_reports', related_query_name='customer_service_report', to='reports.Signature')),
            ],
            options={
                'verbose_name': 'Customer Service',
                'verbose_name_plural': 'Customer Service Reports',
            },
            bases=('reports.report',),
        ),
    ]
