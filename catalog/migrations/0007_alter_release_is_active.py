# Generated by Django 5.1 on 2024-09-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_release_is_active_alter_release_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Укажите является ли версия активной'),
        ),
    ]
