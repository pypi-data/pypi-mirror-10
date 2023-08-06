#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
Any helpers for Pyramid
"""
import itertools

import colander
import sqlalchemy

from sacrud.common import get_attrname_by_colname, get_columns


def preprocessing_value(value):
    if value is colander.null:
        return None
    return value


def import_from_string(path):
    if not isinstance(path, str):
        return path
    parts = path.split(':')
    if not len(parts) > 1:
        return None
    temp = __import__(parts[0], globals(), locals(), [parts[1], ], 0)
    return getattr(temp, parts[1], None)


def pkg_prefix(config):
    '''
    Function for return pkg prefix.

    >>> from pyramid.config import Configurator
    >>> settings = {'foo': 'foo', 'bar': 'bar'}

    # Create config
    >>> config = Configurator(settings=settings)

    # w/o route_prefix
    >>> pkg_prefix(config)
    '/sacrud/'

    # with route_prefix
    >>> config.route_prefix = "/admin"
    >>> pkg_prefix(config)
    ''
    '''
    return '' if config.route_prefix else '/sacrud/'


def _silent_none(value):
    if type(value) == int:
        return value
    if hasattr(value, '__bool__'):
        return value
    if not value:
        return ''
    try:
        if str(value) == 'None':
            return ''
    except UnicodeEncodeError:
        pass
    return value


def set_jinja2_silent_none(config):  # pragma: no cover
    """ if variable is None print '' instead of 'None'
    """
    config.commit()
    jinja2_env = config.get_jinja2_environment()
    jinja2_env.finalize = _silent_none


def get_settings_param(request, name):
    settings = request.registry.settings
    return settings.get(name, {})


def get_obj_from_settings(request, name):
    settings = request
    if not isinstance(request, dict):
        settings = request.registry.settings
    position_model = settings.get(name)
    if isinstance(position_model, str):
        return import_from_string(position_model)
    return position_model


def sacrud_env(fun):
    jinja2_globals = {'str': str, 'getattr': getattr, 'isinstance': isinstance,
                      'get_attrname_by_colname': get_attrname_by_colname,
                      'hasattr': hasattr,
                      'sqlalchemy': sqlalchemy}

    def wrapped(self, *args, **kwargs):
        response = fun(self, *args, **kwargs)
        if hasattr(response, 'update'):
            response.update(jinja2_globals)
            SessionAttributes = {
                'session': self.request.dbsession,
                'table': self.table,
                'columns': get_columns(self.table)
            }
            response.update(SessionAttributes)
        return response
    return wrapped


def get_table(tname, request):
    """ Return table by table name from pyramid_sacrud.models in settings.
    """
    pyramid_sacrud_models = get_settings_param(request,
                                               'pyramid_sacrud.models')
    try:
        models = dict(pyramid_sacrud_models)
    except ValueError:
        models = dict((pyramid_sacrud_models, ))
    finally:
        models = models.values()

    tables = itertools.chain(*models)
    tables = [table for table in tables
              if (table.__tablename__).lower() == tname.lower()]
    if not tables:
        return None
    return tables[0]


def get_table_verbose_name(table):
    if hasattr(table, 'verbose_name'):
        return table.verbose_name
    elif hasattr(table, '__tablename__'):
        return table.__tablename__
    return table.name


def update_difference_object(obj, key, value):
    if isinstance(obj, dict):
        obj.update({key: value})
    else:
        setattr(obj, key, value)
