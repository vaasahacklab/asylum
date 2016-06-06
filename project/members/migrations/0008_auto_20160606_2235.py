# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20160606_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\+358\\d{9}$', message="Phone number must be entered in the format: '+358999999999'.")], verbose_name='Phone number', blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='membershipapplication',
            name='phone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\+358\\d{9}$', message="Phone number must be entered in the format: '+358999999999'.")], verbose_name='Phone number', blank=True, max_length=200),
        ),
    ]
