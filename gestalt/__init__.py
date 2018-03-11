#!/usr/bin/python
# -*- coding: utf-8 -*

"""
    To use the right lazy_settings, edit desired Python environment file and replace variables values as you need.
    On gestalt/default.py file you will find all variables and yours default values. To add another to the project,
    just edit and add on it.
    Is desired that you have at least a "development.py", a "staging.py" and a "production.py" to separate yours
    environments settings.
"""

from os import environ
from os.path import join
from os.path import dirname

from dynaconf import LazySettings

from gestalt import default

PROJECT_NAME = 'GESTALT_SAMPLE'
ENV_VAR_OF_PROJECT = "{project_name}_SETTINGS".format(project_name=PROJECT_NAME)


def set_environment_settings():
    global ENV_VAR_OF_PROJECT

    env = '{env}'.format(env=environ.get('ENV', 'not-set')).lower()
    if env == 'not-set':
        raise ValueError('You must specify a ENV var indicating "DEVELOPMENT", "STAGING" or "PRODUCTION" value.')
    if env not in ['development', 'staging', 'production']:
        raise ValueError('Valid values for ENV var is: "DEVELOPMENT", "STAGING" or "PRODUCTION"')

    env_file = join(dirname(__file__), '{env}.py'.format(env=env))
    environ[ENV_VAR_OF_PROJECT] = env_file


set_environment_settings()
lazy = LazySettings(ENVVAR_FOR_DYNACONF=ENV_VAR_OF_PROJECT)


def get_settings() -> dict:
    """
    Get settings values from dynaconf and returns it as a dict.
    All properties of default.py will be exposed as a key in dict in lowercase
    :rtype: dict
    :return:
    A dict with properties keys and values.
    """
    global lazy

    settings = {}
    keys = [item for item in dir(default) if item in dir(lazy)]
    for key in keys:
        value = getattr(lazy, key)
        settings[key.lower()] = value
    settings['env_var'] = ENV_VAR_OF_PROJECT
    return settings
