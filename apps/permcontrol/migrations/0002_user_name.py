# Generated by Django 2.1 on 2019-02-28 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permcontrol', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, help_text='机房电话', max_length=32, null=True, verbose_name='用户名'),
        ),
    ]