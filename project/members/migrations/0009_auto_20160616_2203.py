# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20160606_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='monthlyPayment',
            field=models.DecimalField(default=20, max_digits=5, blank=True, validators=[django.core.validators.MinValueValidator(5, message='Number must be positive')], decimal_places=2, verbose_name='Monthly fee'),
        ),
        migrations.AlterField(
            model_name='member',
            name='paymentInterval',
            field=models.IntegerField(default=3, verbose_name='Payment interval', validators=[django.core.validators.MinValueValidator(1, message='Number must be more then 1')], blank=True),
        ),
        migrations.AlterField(
            model_name='membershipapplication',
            name='monthlyPayment',
            field=models.DecimalField(default=20, max_digits=5, blank=True, validators=[django.core.validators.MinValueValidator(5, message='Number must be positive')], decimal_places=2, verbose_name='Monthly fee'),
        ),
        migrations.AlterField(
            model_name='membershipapplication',
            name='paymentInterval',
            field=models.IntegerField(default=3, verbose_name='Payment interval', validators=[django.core.validators.MinValueValidator(1, message='Number must be more then 1')], blank=True),
        ),
    ]
