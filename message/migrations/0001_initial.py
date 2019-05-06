# Generated by Django 2.2.1 on 2019-05-06 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0005_auto_20190506_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_sent', models.DateTimeField()),
                ('subject', models.CharField(max_length=255)),
                ('message_body', models.CharField(max_length=999)),
                ('message_seen', models.BooleanField()),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_to', to='user.User')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_from', to='user.User')),
            ],
        ),
    ]