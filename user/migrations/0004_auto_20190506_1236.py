# Generated by Django 2.2.1 on 2019-05-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190506_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='municipiality',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='postal_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_roles',
            field=models.TextField(),
        ),
    ]
