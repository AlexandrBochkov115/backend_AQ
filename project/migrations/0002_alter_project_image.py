# Generated by Django 5.2.1 on 2025-05-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='project/projects/', verbose_name='Изображение'),
        ),
    ]
