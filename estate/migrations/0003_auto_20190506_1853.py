# Generated by Django 2.2.1 on 2019-05-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0002_estateimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='open_house',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
