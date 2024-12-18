# Generated by Django 5.1.1 on 2024-11-12 15:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0013_contribution"),
    ]

    operations = [
        migrations.AlterField(
            model_name="authorbook",
            name="contribution_date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="authorbook",
            name="contribution_summary",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="authorbook",
            name="is_primary_author",
            field=models.BooleanField(),
        ),
        migrations.DeleteModel(
            name="Contribution",
        ),
    ]
