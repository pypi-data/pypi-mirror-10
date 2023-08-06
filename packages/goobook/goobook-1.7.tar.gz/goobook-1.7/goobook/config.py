# -*- coding: UTF-8 -*-
# vim: fileencoding=UTF-8 filetype=python ff=unix et ts=4 sw=4 sts=4 tw=120
# author: Christer Sjöholm -- hcs AT furuvik DOT net

from __future__ import absolute_import

import ConfigParser
import locale
import logging
import oauth2client.client
import os

from .storage import Storage
from os.path import realpath, expanduser

log = logging.getLogger(__name__)

try:
    ENCODING = locale.getpreferredencoding() or 'UTF-8'
except LookupError:
    # Some OS X can give a strange encoding
    ENCODING = 'UTF-8'

TEMPLATE = '''\
# "#" or ";" at the start of a line makes it a comment.
[DEFAULT]
# The following are optional, defaults are shown

# This file is written by the oauth library, and should be kept secure,
# it's like a password to your google contacts.
;oauth_db_filename: ~/.goobook_auth.json

# The client secret file is not really secret.
;client_secret_filename: ~/.goobook_client_secret.json

;cache_filename: ~/.goobook_cache
;cache_expiry_hours: 24
;filter_groupless_contacts: yes

# New contacts will be added to this group in addition to "My Contacts"
# Note that the group has to already exist on google or an error will occur.
# One use for this is to add new contacts to an "Unsorted" group, which can
# be sorted easier than all of "My Contacts".
;default_group:
'''


def read_config(config_file):
    '''Reads the ~/.goobookrc and any authentication data
    returns the configuration as a dictionary.

    '''
    config = Storage({  # Default values
        'cache_filename': '~/.goobook_cache',
        'oauth_db_filename': '~/.goobook_auth.json',
        'client_secret_filename': '~/.goobook_client_secret.json',
        'cache_expiry_hours': '24',
        'filter_groupless_contacts': True,
        'default_group': ''})
    config_file = os.path.expanduser(config_file)
    parser = _get_config(config_file)
    if parser:
        config.get_dict().update(dict(parser.items('DEFAULT', raw=True)))
        # Handle not string fields
        if parser.has_option('DEFAULT', 'filter_groupless_contacts'):
            config.filter_groupless_contacts = parser.getboolean('DEFAULT', 'filter_groupless_contacts')

    # Ensure paths are fully expanded
    config.cache_filename = realpath(expanduser(config.cache_filename))
    config.client_secret_filename = realpath(expanduser(config.client_secret_filename))
    config.oauth_db_filename = realpath(expanduser(config.oauth_db_filename))

    config.store = oauth2client.file.Storage(config.oauth_db_filename)
    config.creds = config.store.get()

    # What terminal encoding to use
    config.encoding = ENCODING

    log.debug(config)
    return config


def _get_config(config_file):
    '''find, read and parse configuraton.'''
    parser = ConfigParser.SafeConfigParser()
    if os.path.lexists(config_file):
        try:
            log.info('Reading config: %s', config_file)
            inp = open(config_file)
            parser.readfp(inp)
            return parser
        except (IOError, ConfigParser.ParsingError), err:
            raise ConfigError("Failed to read configuration %s\n%s" % (config_file, err))
    return None


class ConfigError(StandardError):
    pass
