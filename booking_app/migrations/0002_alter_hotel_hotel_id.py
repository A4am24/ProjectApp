# Generated by Django 5.1.6 on 2025-03-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='hotel_id'),
        ),
    ]
