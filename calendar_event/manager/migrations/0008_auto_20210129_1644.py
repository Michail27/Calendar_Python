# Generated by Django 3.1.5 on 2021-01-29 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_holidays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidays',
            name='holiday_finish',
            field=models.DateTimeField(verbose_name='Окончание праздника'),
        ),
        migrations.AlterField(
            model_name='holidays',
            name='holiday_start',
            field=models.DateTimeField(verbose_name='Начала праздника'),
        ),
    ]
