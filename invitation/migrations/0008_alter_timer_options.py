# Generated by Django 5.0.3 on 2024-03-28 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0007_alter_guest_name_second_guest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timer',
            options={'verbose_name': 'Дата свадьбы', 'verbose_name_plural': 'Дата свадьбы'},
        ),
    ]
