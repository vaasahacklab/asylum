# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20160523_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershipapplication',
            name='monthlymember',
            field=models.BooleanField(verbose_name='I want to apply for a monthly fee', default=True),
        ),
    ]
