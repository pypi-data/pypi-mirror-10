from __future__ import unicode_literals

import operator
import sys

import django
from django.contrib.contenttypes.models import ContentType
from django.utils.functional import LazyObject, new_method_proxy

# TODO: Remove the following when support for Python 2.6 is dropped
if sys.version_info >= (2, 7):
    from unittest import skipUnless  # NOQA
else:
    from django.utils.unittest import skipUnless  # NOQA

# TODO: Remove the following when support for Django 1.8 is dropped
if django.VERSION >= (1, 9):
    def get_remote_field(field):
        return field.remote_field

    def get_remote_model(remote_field):
        return remote_field.model
else:
    def get_remote_field(field):
        return field.rel

    def get_remote_model(remote_field):
        return remote_field.to

try:
    from django.db.models.fields.related import lazy_related_operation
except ImportError:
    from django.db.models.fields.related import add_lazy_relation

    def lazy_related_operation(function, model, related_model, field):
        def operation(field, related, local):
            return function(local, related, field)
        add_lazy_relation(model, field, related_model, operation)

# TODO: Remove the following when supports for Django 1.5 is dropped
if django.VERSION >= (1, 6):
    def get_queryset(manager, *args, **kwargs):
        return manager.get_queryset(*args, **kwargs)
else:
    def get_queryset(manager, *args, **kwargs):
        return manager.get_query_set(*args, **kwargs)


if django.VERSION >= (1, 6):
    def model_name(opts):
        return opts.model_name
else:
    def model_name(opts):
        return opts.module_name

if django.VERSION < (1, 6):
    class LazyObject(LazyObject):
        # Dictionary methods support
        __getitem__ = new_method_proxy(operator.getitem)
        __setitem__ = new_method_proxy(operator.setitem)
        __delitem__ = new_method_proxy(operator.delitem)

        __len__ = new_method_proxy(len)
        __contains__ = new_method_proxy(operator.contains)

# TODO: Remove the following when support for Django 1.4 is dropped
try:
    from django.db.models.constants import LOOKUP_SEP  # NOQA
except ImportError:
    from django.db.models.sql.constants import LOOKUP_SEP  # NOQA

# Prior to #18399 being fixed there was no way to retrieve `ContentType`
# of proxy models while caching it. This is a shim that tries to use the
# newly introduced flag and fallback to another method.
# TODO: Remove when support for Django 1.4 is dropped
if django.VERSION >= (1, 5):
    # django 1.5 introduced the `for_concrete_models?` kwarg
    def get_content_type(model, db=None):
        manager = ContentType.objects.db_manager(db)
        return manager.get_for_model(model, for_concrete_model=False)

    def get_content_types(models, db=None):
        manager = ContentType.objects.db_manager(db)
        return manager.get_for_models(*models, for_concrete_models=False)
else:
    from django.utils.encoding import smart_unicode

    def _get_for_proxy_model(manager, opts, model):
        if model._deferred:
            opts = opts.proxy_for_model._meta
        try:
            return manager._get_from_cache(opts)
        except KeyError:
            ct, _created = manager.get_or_create(
                app_label=opts.app_label,
                model=opts.object_name.lower(),
                defaults={'name': smart_unicode(opts.verbose_name_raw)},
            )
            manager._add_to_cache(manager.db, ct)
            return ct

    def get_content_type(model, db=None):
        manager = ContentType.objects.db_manager(db)
        opts = model._meta
        if opts.proxy:
            return _get_for_proxy_model(manager, opts, model)
        else:
            return manager.get_for_model(model)

    def get_content_types(models, db=None):
        manager = ContentType.objects.db_manager(db)
        content_types = {}
        concrete_models = []
        for model in models:
            opts = model._meta
            if opts.proxy:
                content_type = _get_for_proxy_model(manager, opts, model)
                content_types[model] = content_type
            else:
                concrete_models.append(model)
        content_types.update(manager.get_for_models(*concrete_models))
        return content_types

string_types = str if sys.version_info[0] == 3 else basestring


def with_metaclass(meta, *bases):
    class metaclass(meta):
        __call__ = type.__call__
        __init__ = type.__init__

        def __new__(cls, name, this_bases, d):
            if this_bases is None:
                return type.__new__(cls, name, (), d)
            return meta(name, bases, d)
    return metaclass(str('temporary_class'), None, {})
