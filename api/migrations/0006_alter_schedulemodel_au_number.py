# Generated by Django 3.2.9 on 2021-11-14 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_schedulemodel_au_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulemodel',
            name='au_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]