# Generated by Django 4.0.5 on 2022-11-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scans', '0004_rename_github_secrets_cms_cms_cms_subdomain_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtakeover',
            name='takeover',
        ),
        migrations.AddField(
            model_name='subtakeover',
            name='subdomain',
            field=models.CharField(blank=True, default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='subtakeover',
            name='type_takeover',
            field=models.CharField(blank=True, default='N/A', max_length=100),
        ),
        migrations.DeleteModel(
            name='SubdomainsConsolidated',
        ),
    ]
