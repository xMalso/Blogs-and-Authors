# Generated by Django 5.1.2 on 2024-11-10 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_authorbook_contribution_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorbook',
            name='contribution_summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
