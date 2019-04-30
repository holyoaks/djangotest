import os
import posixpath
import stat
import urllib.request, urllib.parse, urllib.error

from django import template
from django.conf import settings
from django.contrib.staticfiles import finders

register = template.Library()

@register.simple_tag
def staticfile(path):
    normalized_path = posixpath.normpath(urllib.parse.unquote(path)).lstrip('/')
    absolute_path = finders.find(normalized_path)
    if not absolute_path and getattr(settings, 'STATIC_ROOT', None):
        absolute_path = os.path.join(settings.STATIC_ROOT, path)
    if absolute_path:
        return '%s%s?v=%s' % (settings.STATIC_URL, path, os.stat(absolute_path)[stat.ST_MTIME])
    return path