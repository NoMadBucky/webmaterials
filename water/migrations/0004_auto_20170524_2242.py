# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-24 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0003_auto_20170524_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effluent_data',
            name='days_late',
            field=models.FloatField(default=0, null=True, verbose_name='Days Late'),
        ),
        migrations.AlterField(
            model_name='effluent_data',
            name='dmr_value_nmbr',
            field=models.FloatField(default=0, verbose_name='DMR Value'),
        ),
        migrations.AlterField(
            model_name='effluent_data',
            name='dmr_value_standard_units',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='effluent_data',
            name='exceedance_pct',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='effluent_data',
            name='limit_id',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='effluent_data',
            name='npdes_id',
            field=models.CharField(default='NA', max_length=9, verbose_name='Permit Number'),
        ),
        migrations.AlterField(
            model_name='effluent_data',
            name='npdes_violation_id',
            field=models.IntegerField(default=0, verbose_name='Violation Number'),
        ),
        migrations.AlterField(
            model_name='effluent_data',
            name='parameter_desc',
            field=models.CharField(default='NA', max_length=100, verbose_name='Parameter Description'),
        ),
        migrations.AlterField(
            model_name='effluent_data',
            name='rnc_detection_desc',
            field=models.CharField(blank=True, max_length=100, verbose_name='Noncompliance Description'),
        ),
        migrations.AlterField(
            model_name='effluent_data',
            name='value_received_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date Reported'),
        ),
        migrations.AlterField(
            model_name='effluent_data',
            name='violation_code',
            field=models.CharField(default='NA', max_length=5, verbose_name='Violation Code'),
        ),
        migrations.AlterField(
            model_name='effluent_data',
            name='violation_desc',
            field=models.CharField(default='NA', max_length=100, verbose_name='Violation Description'),
        ),
    ]
