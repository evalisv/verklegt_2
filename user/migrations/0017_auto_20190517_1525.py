# Generated by Django 2.2.1 on 2019-05-17 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20190516_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]