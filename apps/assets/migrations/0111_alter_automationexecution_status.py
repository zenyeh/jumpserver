# Generated by Django 3.2.14 on 2022-11-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0110_changesecretrecord_asset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automationexecution',
            name='status',
            field=models.CharField(default='pending', max_length=16, verbose_name='Status'),
        ),
    ]
