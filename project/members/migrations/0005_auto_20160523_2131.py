# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20151229_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='monthlyPayment',
            field=models.DecimalField(decimal_places=2, verbose_name='Monthly fee', blank=True, max_digits=5, default=5, validators=[django.core.validators.MinValueValidator(5, message='Number must be positive')]),
        ),
        migrations.AddField(
            model_name='member',
            name='paymentInterval',
            field=models.IntegerField(verbose_name='Payment interval', blank=True, validators=[django.core.validators.MinValueValidator(1, message='Number must be positive')], default=3),
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='monthlyPayment',
            field=models.DecimalField(decimal_places=2, verbose_name='Monthly fee', blank=True, max_digits=5, default=5, validators=[django.core.validators.MinValueValidator(5, message='Number must be positive')]),
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='paymentInterval',
            field=models.IntegerField(verbose_name='Payment interval', blank=True, validators=[django.core.validators.MinValueValidator(1, message='Number must be positive')], default=3),
        ),
    ]
