# Generated by Django 5.2.1 on 2025-05-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0004_delete_pooladvantagedescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poolimage',
            name='description',
        ),
        migrations.AddField(
            model_name='pool',
            name='description_short',
            field=models.TextField(blank=True, help_text='Короткое описание (до 300 символов)', verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='pool',
            name='description',
            field=models.TextField(verbose_name='Полное описание'),
        ),
    ]
