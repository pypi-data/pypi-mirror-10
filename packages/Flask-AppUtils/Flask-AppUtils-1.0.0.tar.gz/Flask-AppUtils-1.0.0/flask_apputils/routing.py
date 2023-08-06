# -*- coding: utf-8 -*-
"""
    flask_apputils.routing
    ~~~~~~~~~~~~~~~~~~~~~~

    Utilities for building route handlers
"""

from werkzeug.utils import import_string, cached_property
from flask.blueprints import Blueprint
from .decorators import as_json, with_request_body, with_template

__all__ = (
    'APIBlueprint',
    'TemplateBlueprint',
    'LazyView',
    'make_router'
)


class LazyView(object):
    def __init__(self, import_name):
        self.__module__, self.__name__ = import_name.rsplit('.', 1)
        self.import_name = import_name

    @cached_property
    def view(self):
        return import_string(self.import_name)

    def __call__(self, *args, **kwargs):
        return self.view(*args, **kwargs)


def make_router(blueprint, import_prefix=None, filters=None):
    """
    Create a router function that lazily load and dispatch routes on the app or blueprint

    ..code: python

        # using filters `require_login`
        route = make_router(app, require_login)
        route('/load-data', 'myapp.dashboard.add_user', methods=['GET'])

    :param blueprint: the app or blueprint
    :param filters: middleware list in order that wrap the request handlers
    :return:
    """

    def router(url_rule, func_name, endpoint=None, **options):
        """
        Register route urls and handlers

        :param url_rule: route url rule
        :param func_name: handler function
        :param options: route options
        :return:
        """
        if import_prefix:
            func_name = import_prefix + '.' + func_name

        view = LazyView(func_name)

        # wrap filters
        if filters:
            assert isinstance(filters, (tuple, list))
            for f in filters:
                view = f(view)

        endpoint = endpoint or func_name.split('.')[-1]
        blueprint.add_url_rule(url_rule, endpoint, view_func=view, **options)

    return router


class APIBlueprint(Blueprint):
    """
    Blueprint which inject request body into handler and return responses as JSON.
    """

    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        view_func = as_json(with_request_body(view_func))
        return super(APIBlueprint, self).add_url_rule(rule, endpoint, view_func, **options)


class TemplateBlueprint(Blueprint):
    """Blueprint which loads and render templates with response data as context

    The template directory corresponds to the name of the blueprint in the `app.template_folder`
    """

    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        tpl_func = with_template('/'.join([self.name, view_func.__name__]))
        view_func = tpl_func(view_func)
        return super(TemplateBlueprint, self).add_url_rule(rule, endpoint, view_func, **options)
