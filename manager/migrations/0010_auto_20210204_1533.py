# Generated by Django 3.1.5 on 2021-02-04 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_auto_20210129_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='createevent',
            name='notification',
            field=models.BooleanField(default=False, verbose_name='Оповещение'),
        ),
        migrations.AlterField(
            model_name='createevent',
            name='reminder',
            field=models.CharField(blank=True, choices=[(datetime.timedelta(seconds=3600), 'За час'), (datetime.timedelta(seconds=7200), 'За 2 часа'), (datetime.timedelta(seconds=14400), 'За 4 часа'), (datetime.timedelta(days=1), 'За день'), (datetime.timedelta(days=7), 'За неделю')], max_length=50, null=True, verbose_name='Когда напомнить'),
        ),
    ]
