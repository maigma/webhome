# Generated by Django 2.0.2 on 2018-03-06 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180306_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appusersmodel',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='appusersmodel',
            name='last_login',
        ),
    ]