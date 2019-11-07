# Generated by Django 2.2.7 on 2019-11-07 14:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goalkeeper', '0002_auto_20191107_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 11, 7, 14, 57, 0, 590170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='history',
            name='target',
            field=models.IntegerField(),
        ),
    ]