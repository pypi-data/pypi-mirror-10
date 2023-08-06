# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The qiita Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------
import os
from sys import stderr
from uuid import uuid4

from redis import Redis
from future import standard_library
from IPython.parallel.error import TimeoutError
with standard_library.hooks():
    from configparser import ConfigParser

from moi.context import Context  # noqa


def _support_directory():
    """Get the path of the support_files directory"""
    from os.path import join, dirname, abspath
    return join(dirname(abspath(__file__)), 'support_files')


def moi_js():
    """Return the absolute path to moi.js"""
    from os.path import join
    return join(_support_directory(), 'moi.js')


def moi_list_js():
    """Return the absolute path to moi_list.js"""
    from os.path import join
    return join(_support_directory(), 'moi_list.js')


REDIS_KEY_TIMEOUT = 84600 * 14  # two weeks


# parse the config bits
if 'MOI_CONFIG_FP' not in os.environ:
    raise IOError('$MOI_CONFIG_FP is not set')

_config = ConfigParser()
with open(os.environ['MOI_CONFIG_FP']) as conf:
    _config.readfp(conf)


# establish a connection to the redis server
r_client = Redis(host=_config.get('redis', 'host'),
                 port=_config.getint('redis', 'port'),
                 password=_config.get('redis', 'password'),
                 db=_config.get('redis', 'db'))

# make sure we can connect, let the error propogate so it can be caught
# or observed upstrean
key = 'MOI_INIT_TEST_%s' % str(uuid4())
r_client.set(key, 42)
r_client.delete(key)

# setup contexts
ctxs = {}
failed = []
for name in _config.get('ipython', 'context').split(','):
    try:
        ctxs[name] = Context(name)
    except (TimeoutError, IOError, ValueError):
        failed.append(name)

if failed:
    stderr.write('Unable to connect to ipcluster(s): %s\n' % ', '.join(failed))

ctx_default = _config.get('ipython', 'default')


__version__ = '0.2.0'
__all__ = ['r_client', 'ctxs', 'ctx_default', 'REDIS_KEY_TIMEOUT', 'moi_js',
           'moi_list_js']
