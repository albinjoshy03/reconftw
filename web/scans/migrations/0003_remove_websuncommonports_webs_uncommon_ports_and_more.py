# Generated by Django 4.0.5 on 2022-11-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scans', '0002_screenshots_hostname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websuncommonports',
            name='webs_uncommon_ports',
        ),
        migrations.AddField(
            model_name='websuncommonports',
            name='host',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='websuncommonports',
            name='ports',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
