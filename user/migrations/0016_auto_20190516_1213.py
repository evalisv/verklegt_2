# Generated by Django 2.2.1 on 2019-05-16 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20190512_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.FileField(blank=True, max_length=9999, null=True, upload_to='media/users'),
        ),
    ]
