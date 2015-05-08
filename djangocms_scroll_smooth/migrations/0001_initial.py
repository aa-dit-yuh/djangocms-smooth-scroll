# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmoothScrollPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('easing', models.CharField(default=b'linear', max_length=25, choices=[(b'linear', 'linear'), (b'easeInQuad', 'easeInQuad'), (b'easeInCubic', 'easeInCubic'), (b'easeInQuart', 'easeInQuart'), (b'easeInQuint', 'easeInQuint'), (b'easeInOutQuad', 'easeInOutQuad'), (b'easeInOutCubic', 'easeInOutCubic'), (b'easeInOutQuart', 'easeInOutQuart'), (b'easeInOutQuint', 'easeInOutQuint'), (b'easeOutQuad', 'easeOutQuad'), (b'easeOutCubic', 'easeOutCubic'), (b'easeOutQuart', 'easeOutQuart'), (b'easeOutQuint', 'easeOutQuint')])),
                ('display_text', models.CharField(default=b'', help_text='Please supply the text to be displayed by the link', max_length=32, verbose_name=b'Text of the Link')),
                ('scrollto_id', models.CharField(default=b'', help_text='Please supply the id of the element to which it should scroll', max_length=32, verbose_name=b'Scroll To ID')),
                ('speed', models.PositiveIntegerField(help_text='Speed of the scroll', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
