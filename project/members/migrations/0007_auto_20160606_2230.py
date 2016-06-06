# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_membershipapplication_monthlymember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(verbose_name='Phone number', validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+358999999999'.", regex='^\\+358\\d{9-15}$')], blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='membershipapplication',
            name='phone',
            field=models.CharField(verbose_name='Phone number', validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+358999999999'.", regex='^\\+358\\d{9-15}$')], blank=True, max_length=200),
        ),
    ]
