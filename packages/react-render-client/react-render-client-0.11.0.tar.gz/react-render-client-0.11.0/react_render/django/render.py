from __future__ import absolute_import

import os
from django.contrib.staticfiles import finders
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe
from django.conf import settings
from react_render.core import render_component as render_core
from react_render.core import DEFAULT_SERVICE_URL

SERVICE_URL = getattr(settings, 'REACT_SERVICE_URL', DEFAULT_SERVICE_URL)


class RenderedComponent(object):
    def __init__(self, output, path_to_source, props, json_encoder):
        self.output = output
        self.path_to_source = path_to_source
        self.props = props
        self.json_encoder = json_encoder

    def __str__(self):
        return mark_safe(self.output)

    def __unicode__(self):
        return mark_safe(self.output)

    def render_props(self):
        if self.props:
            return mark_safe(self.json_encoder(self.props))
        return '{}'


def render_component(path_to_source, props=None, to_static_markup=False, json_encoder=None):
    if not os.path.isabs(path_to_source):
        path_to_source = finders.find(path_to_source) or path_to_source

    if json_encoder is None:
        json_encoder = DjangoJSONEncoder().encode

    html = render_core(path_to_source, props, to_static_markup, json_encoder, service_url=SERVICE_URL)

    return RenderedComponent(html, path_to_source, props, json_encoder)
