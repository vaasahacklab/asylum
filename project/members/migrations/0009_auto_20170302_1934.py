# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20160606_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='monthlyPayment',
            field=models.DecimalField(default=20, max_digits=5, blank=True, validators=[django.core.validators.MinValueValidator(5, message='Number must be positive')], verbose_name='Monthly fee', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='member',
            name='paymentInterval',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Number must be more then 1')], default=3, verbose_name='Payment interval', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Phone number', blank=True),
        ),
        migrations.AlterField(
            model_name='membershipapplication',
            name='monthlyPayment',
            field=models.DecimalField(default=20, max_digits=5, blank=True, validators=[django.core.validators.MinValueValidator(5, message='Number must be positive')], verbose_name='Monthly fee', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='membershipapplication',
            name='paymentInterval',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Number must be more then 1')], default=3, verbose_name='Payment interval', blank=True),
        ),
        migrations.AlterField(
            model_name='membershipapplication',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Phone number', blank=True),
        ),
    ]
