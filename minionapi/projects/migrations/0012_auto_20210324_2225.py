# Generated by Django 2.2.15 on 2021-03-24 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20210324_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['index', '-created_at']},
        ),
        migrations.AddField(
            model_name='update',
            name='status',
            field=models.CharField(choices=[('URGENT', 'Urgent'), ('INFO', 'Informational'), ('REMARK', 'Remark'), ('POSITIVE', 'Positive')], default='INFO', max_length=32),
        ),
    ]