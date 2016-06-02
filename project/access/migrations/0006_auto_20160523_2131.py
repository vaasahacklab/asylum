# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0005_auto_20151226_1816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accesstype',
            options={'verbose_name': 'Access Type', 'verbose_name_plural': 'Access Types', 'ordering': ['label']},
        ),
        migrations.AlterModelOptions(
            name='grant',
            options={'verbose_name': 'Grant', 'verbose_name_plural': 'Grants', 'ordering': ['owner__lname', 'owner__fname', 'atype__label']},
        ),
        migrations.AlterModelOptions(
            name='nonmembertoken',
            options={'verbose_name': 'Non-member token', 'verbose_name_plural': 'Non-member tokens', 'ordering': ['contact', 'ttype__label']},
        ),
        migrations.AlterModelOptions(
            name='token',
            options={'verbose_name': 'Token', 'verbose_name_plural': 'Tokens', 'ordering': ['owner__lname', 'owner__fname', 'ttype__label']},
        ),
        migrations.AlterModelOptions(
            name='tokentype',
            options={'verbose_name': 'Token Type', 'verbose_name_plural': 'Token Types', 'ordering': ['label']},
        ),
    ]
