# Generated by Django 3.2.14 on 2022-12-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0114_remove_redundant_macos'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountbackupplan',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='baseautomation',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='changesecretrecord',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='domain',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='domain',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='domain',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='favoriteasset',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='favoriteasset',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='gathereduser',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='gathereduser',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='gathereduser',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='node',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='node',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='node',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created'),
        ),
        migrations.AddField(
            model_name='node',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='node',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='account',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='account',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='accountbackupplan',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='accountbackupplan',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='accounttemplate',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='accounttemplate',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='baseautomation',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='baseautomation',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='changesecretrecord',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='changesecretrecord',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='favoriteasset',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='gathereduser',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created'),
        ),
        migrations.AlterField(
            model_name='label',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='label',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='label',
            name='updated_by',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by'),
        ),
    ]
