# Generated by Django 3.2.16 on 2023-01-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0024_alter_menuitem_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='num_seats',
            field=models.IntegerField(choices=[(2, '2'), (4, '4'), (5, '5'), (6, '6')], default=2),
        ),
    ]
