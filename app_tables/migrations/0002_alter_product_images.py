# Generated by Django 4.2.7 on 2023-11-06 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(unique=True, upload_to='acc/'),
        ),
    ]