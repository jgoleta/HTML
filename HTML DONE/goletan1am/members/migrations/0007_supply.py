# Generated by Django 5.2 on 2025-05-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supply_id', models.CharField(max_length=20, unique=True)),
                ('supplier', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
