# Generated by Django 5.1.1 on 2024-11-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_authorbook_contribution_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorbook',
            name='is_primary_author',
        ),
        migrations.AddField(
            model_name='book',
            name='fiction',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
