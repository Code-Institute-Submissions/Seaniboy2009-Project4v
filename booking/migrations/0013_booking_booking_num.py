# Generated by Django 3.2.16 on 2023-01-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_num',
            field=models.CharField(default='00000', max_length=5, unique=True),
        ),
    ]
