# Generated by Django 5.2 on 2025-05-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_id', models.CharField(max_length=20)),
                ('order_id', models.CharField(max_length=20)),
                ('customer', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('scheduled_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
