# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SmoothScrollPluginModel'
        db.create_table(u'djangocms_scroll_smooth_smoothscrollpluginmodel', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('easing', self.gf('django.db.models.fields.CharField')(default='linear', max_length=25)),
            ('display_text', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('scrollto_id', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('speed', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'djangocms_scroll_smooth', ['SmoothScrollPluginModel'])


    def backwards(self, orm):
        # Deleting model 'SmoothScrollPluginModel'
        db.delete_table(u'djangocms_scroll_smooth_smoothscrollpluginmodel')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'djangocms_scroll_smooth.smoothscrollpluginmodel': {
            'Meta': {'object_name': 'SmoothScrollPluginModel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'display_text': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'easing': ('django.db.models.fields.CharField', [], {'default': "'linear'", 'max_length': '25'}),
            'scrollto_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            'speed': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['djangocms_scroll_smooth']