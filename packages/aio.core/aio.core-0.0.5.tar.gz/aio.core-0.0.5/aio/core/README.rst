aio.core.exceptions usage
=========================


MissingConfiguration
--------------------

>>> from configparser import ConfigParser
>>> from aio.core.exceptions import MissingConfiguration

>>> def get_configuration(conf, section, option):
...     try:
...         conf[section][option]
...     except KeyError:
...         raise MissingConfiguration(
...             "Configuration option is missing: %s:%s" % (
...                 section, option))
  
>>> try:
...     get_configuration(ConfigParser(), "foo", "bar")
... except MissingConfiguration as e:
...     print(e)
Configuration option is missing: foo:bar


BadConfiguration
--------------------  
  
>>> from aio.core.exceptions import BadConfiguration  

>>> def get_configuration(conf, section, option, option_type):
...     option_value = conf[section][option]
...     try:
...         option_type(option_value)
...     except ValueError:
...         raise BadConfiguration(
...             'Configuration is bad: %s:%s expected type %s, but got "%s"' % (
...                 section, option, option_type.__name__, option_value))

>>> config = ConfigParser()
>>> config.read_dict({"foo": {"bar": "baz"}})

>>> try:
...     get_configuration(config, "foo", "bar", int)
... except BadConfiguration as e:
...     print(e)
Configuration is bad: foo:bar expected type int, but got "baz"
