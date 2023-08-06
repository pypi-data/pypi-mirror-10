# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RenderitCMSPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(
                    to='cms.CMSPlugin', parent_link=True, serialize=False,
                    auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
