# Generated by Django 3.1.3 on 2020-11-12 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unica_app', '0004_auto_20201112_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='numerohistorico',
            name='port',
            field=models.IntegerField(default=-1),
        ),
    ]
