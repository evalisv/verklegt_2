# Generated by Django 2.2.1 on 2019-05-06 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190506_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='estates',
        ),
        migrations.RemoveField(
            model_name='user',
            name='messages',
        ),
        migrations.RemoveField(
            model_name='user',
            name='municipiality',
        ),
        migrations.RemoveField(
            model_name='user',
            name='offers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_roles',
        ),
    ]
