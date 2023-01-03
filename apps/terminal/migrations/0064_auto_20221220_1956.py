# Generated by Django 3.2.14 on 2022-12-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0063_applet_builtin'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandstorage',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='replaystorage',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='sessionjoinrecord',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='sessionjoinrecord',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='sessionreplay',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='sessionreplay',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='sessionsharing',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='sessionsharing',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='task',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='task',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='task',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='task',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='terminal',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='terminal',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='terminal',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='applet',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='applet',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='applethostdeployment',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='applethostdeployment',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='appletpublication',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='appletpublication',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='commandstorage',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='endpointrule',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='endpointrule',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='replaystorage',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='sessionjoinrecord',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='sessionreplay',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='sessionsharing',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created'),
        ),
        migrations.AlterField(
            model_name='terminal',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='terminal',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created'),
        ),
    ]