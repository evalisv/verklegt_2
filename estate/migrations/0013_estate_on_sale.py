# Generated by Django 2.2.1 on 2019-05-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0012_auto_20190510_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='on_sale',
            field=models.BooleanField(default=True),
        ),
    ]