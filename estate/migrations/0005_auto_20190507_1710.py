# Generated by Django 2.2.1 on 2019-05-07 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0004_estatetype_municipality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='postal_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.Municipality'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.EstateType'),
        ),
    ]
