# -*- coding: utf-8 -*-
import json
import sqlite3
from collections import defaultdict

from access.utils import all_tokens
from members.models import Member as Members
from access.models import AccessType as atypes
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Exports tokens and their access controls to JSON feed'

    def add_arguments(self, parser):
        parser.add_argument('filepath')
        parser.add_argument('atypeLabel')

    def handle(self, *args, **options):
        output_export = {}
        for member in Members.objects.filter(access_granted__atype__in=atypes.objects.filter(label=options['atypeLabel'])):
            memberFilter = {}
            memberFilter["owner_id"] = member.pk
            output_export[member.anonymized_id] = defaultdict(list)
            output_export[member.anonymized_id]["Access"] = member.access_acl
            output_export[member.anonymized_id]["nick"] = member.nick
            for t in all_tokens(tfilters=memberFilter):
                if not t.revoked:
                    acl = t.acl
                    output_export[member.anonymized_id][t.ttype.label].append(t.value)
                    print('Value: {0}, TypePK: {1}, Bits: {2}, Externals: {3}'.format(t.value, t.ttype.label, acl['bits'],
                                                                                      json.dumps(acl['externals'])))
        print(json.dumps(output_export))
