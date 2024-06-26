# Generated by Django 5.0.3 on 2024-04-18 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='QuantityRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_qty', models.IntegerField()),
                ('end_qty', models.IntegerField()),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=6)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quantity_ranges', to='calculator.device')),
            ],
        ),
    ]
