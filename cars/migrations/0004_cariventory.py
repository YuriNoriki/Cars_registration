# Generated by Django 5.1.6 on 2025-04-29 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_photo_car_plate'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarIventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_count', models.IntegerField()),
                ('car_value', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-create_at'],
            },
        ),
    ]
