# Generated by Django 5.2.1 on 2025-05-21 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/', verbose_name='Изображение'),
        ),
    ]
