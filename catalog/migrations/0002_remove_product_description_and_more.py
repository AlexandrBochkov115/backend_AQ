# Generated by Django 5.2.1 on 2025-05-14 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='generator_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='installation_method',
        ),
        migrations.RemoveField(
            model_name='product',
            name='reliability',
        ),
        migrations.RemoveField(
            model_name='product',
            name='special_notes',
        ),
        migrations.AddField(
            model_name='productcharacteristic',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
