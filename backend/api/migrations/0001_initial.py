# Generated by Django 5.1.2 on 2024-11-08 23:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AuthorBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution_type', models.CharField(max_length=100)),
                ('is_primary_author', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.author')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('authors', models.ManyToManyField(through='api.AuthorBook', to='api.author')),
            ],
        ),
        migrations.AddField(
            model_name='authorbook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.book'),
        ),
    ]