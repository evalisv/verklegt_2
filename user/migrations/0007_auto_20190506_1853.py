# Generated by Django 2.2.1 on 2019-05-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='watchlist',
            field=models.TextField(blank=True, null=True),
        ),
    ]