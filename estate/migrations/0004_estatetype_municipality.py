# Generated by Django 2.2.1 on 2019-05-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0003_auto_20190506_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstateType',
            fields=[
                ('type', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('postal_code', models.IntegerField(primary_key=True, serialize=False)),
                ('municipality', models.CharField(max_length=255)),
            ],
        ),
    ]
