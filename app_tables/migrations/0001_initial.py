# Generated by Django 4.2.7 on 2023-11-06 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='motorcycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=15)),
                ('motorcycle', models.CharField(max_length=15)),
                ('year', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=9, unique=True)),
                ('images', models.ImageField(upload_to='acc/')),
                ('accessory', models.CharField(max_length=30)),
                ('compatibility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tables.motorcycle')),
            ],
        ),
        migrations.CreateModel(
            name='compatibility_acc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='coded', to='app_tables.product')),
                ('code_ref', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app_tables.product')),
            ],
        ),
    ]
