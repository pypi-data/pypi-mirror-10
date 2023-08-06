# No shebang line, this module is meant to be imported
#
# Copyright 2014 Oliver Palmer
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Template
--------

Interface methods for working with the Jinja template
engine.
"""

from io import BytesIO

from jinja2 import (
    Environment as _Environment, Template as _Template,
    PackageLoader, BytecodeCache)

from pyfarm.agent.config import config


class InMemoryCache(BytecodeCache):
    """
    Caches Jinja templates into memory after they have been loaded
    and compiled.
    """
    cache = {}

    def clear(self):
        self.cache.clear()

    # Untested as this is an internal implementation for
    # the Environment class below.
    def load_bytecode(self, bucket):  # pragma: no cover
        if bucket.key in self.cache:
            bucket.load_bytecode(self.cache[bucket.key])

    # Untested as this is an internal implementation for
    # the Environment class below.
    def dump_bytecode(self, bucket):  # pragma: no cover
        cache = BytesIO()
        bucket.write_bytecode(cache)
        self.cache[bucket.key] = cache


class Environment(_Environment):
    """
    Implementation of :class:`jinja2.Environment` class which
    reads from our configuration object and establishes the
    default functions we can use in a template.
    """

    def __init__(self, **kwargs):
        # default options
        kwargs.setdefault("bytecode_cache", InMemoryCache())
        kwargs.setdefault("loader", PackageLoader("pyfarm.agent.http"))
        kwargs.setdefault("auto_reload", config["agent_html_template_reload"])

        super(Environment, self).__init__(**kwargs)

        # global functions which are available within
        # the templates
        self.globals.update(
            is_int=lambda value: isinstance(value, int),
            is_str=lambda value: isinstance(value, (str, unicode)),
            typename=lambda value: type(value).__name__,
            agent_hostname=lambda: config["agent_hostname"],
            agent_id=lambda: config["agent_id"],
            state=lambda: config["state"],
            repr=repr)


try:
    ENVIRONMENT
except NameError:  # pragma: no cover
    ENVIRONMENT = Environment()

load = ENVIRONMENT.get_template
