#!/usr/bin/python
# -*- coding: utf-8 -*

from os import environ

from gestalt import get_settings
from gestalt import lazy
from gestalt import default


def try_get_settings():
    settings = {}
    try:
        print('getting settings.')
        settings = get_settings()
        print('\n{name}\n\nProperties:'.format(name=settings.get('application_name')))
        keys = [item.lower() for item in dir(default) if not item.startswith('_')]
        for key in [key for key in keys if key in settings]:
            value = settings[key]
            print('\t{key} - {type} - {value}'.format(key=key, value=value, type=type(value)))
    except Exception as ex:
        print(str(ex))
    finally:
        print('\nUsed config file: {file}'.format(file=environ.get(settings.get('env_var'))))


def try_lazy():
    try:
        print('getting lazy settings.')
        print('\n{name}\n\nProperties:'.format(name=lazy.APPLICATION_NAME))
        # filter only items that start with upper case letter to ignore package items.
        keys = [item for item in dir(default) if item in dir(lazy) and not item.startswith('_')]
        for key in keys:
            value = getattr(lazy, key)
            print('\t{key} - {type} - {value}'.format(key=key, value=value, type=type(value)))
    except Exception as ex:
        print(str(ex))
    finally:
        print('\nUsed config file: {file}'.format(file=environ.get(lazy.ENVVAR_FOR_DYNACONF)))


def main():
    try_lazy()
    try_get_settings()


if __name__ == '__main__':
    main()
