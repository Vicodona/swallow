# Generated by Django 2.1 on 2019-01-28 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinet',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idc.Idc', verbose_name='所处机房'),
        ),
    ]
