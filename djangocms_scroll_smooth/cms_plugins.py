from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import SmoothScrollPluginModel


class SmoothScrollPlugin(CMSPluginBase):
    name = _('Smooth Scroll')
    model = SmoothScrollPluginModel
    render_template = 'djangocms_smoothscroll/_djangocms_smoothscroll_plugin.html'
    text_enabled = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(SmoothScrollPlugin)