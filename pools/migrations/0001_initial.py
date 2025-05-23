# Generated by Django 5.2.1 on 2025-05-17 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('main_image', models.ImageField(upload_to='pools/main/')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PoolAdvantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advantages', to='pools.pool')),
            ],
        ),
        migrations.CreateModel(
            name='PoolImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pools/gallery/')),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pools.pool')),
            ],
        ),
    ]
