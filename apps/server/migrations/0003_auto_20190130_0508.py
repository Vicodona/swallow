# Generated by Django 2.1 on 2019-01-29 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20190130_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='disk_capacity',
            field=models.DecimalField(decimal_places=2, help_text='磁盘容量(GB)', max_digits=10, verbose_name='磁盘容量(GB)'),
        ),
    ]
