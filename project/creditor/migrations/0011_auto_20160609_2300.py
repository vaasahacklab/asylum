# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('creditor', '0010_auto_20160526_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='endDate',
            field=models.DateField(db_index=True, default=django.utils.timezone.now, verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='rcreator',
            field=models.ForeignKey(to='creditor.RecurringTransaction', related_name='creditor_transactions', blank=True, null=True, verbose_name='Recurring Transaction'),
        ),
    ]
