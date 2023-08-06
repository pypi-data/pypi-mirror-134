# SPDX-FileCopyrightText: 2019-2021 Freemelt AB <opensource@freemelt.com>
#
# SPDX-License-Identifier: LGPL-3.0-only

"""This module handles service configuration files.

This module defines the class `Configurator` which can be used to find and
load a configuration file. The file types supported are currently JSON and
YAML.

Note: This module requires Python 3.6 or newer (because f-strings are used).
"""

# Built-in
import logging
import json
import functools
import operator
from pathlib import Path
from pprint import pformat

# PyPI
import yaml

__version__ = '@VERSION@'
log = logging.getLogger(__name__)


class Configurator:
    """Use :meth:`load_config()` to creating an instance of this class"""

    def __init__(self, block: dict, delimiter=':'):
        """Initialize an instance of the Configurator

        **Note**: You should normally create an instance by using the
        :meth:`load_config()` constructor.

        :param block: Dictionary of configuration.
        :param delimiter: The delimiter used to separate keys.
        """
        self.block = block
        self.delimiter = delimiter

    @classmethod
    def load_config(cls, file, search_paths=('/etc/freemelt', '.')):
        """Search for configuration `file` in `search_paths` and load it.

        This is the normal way of creating an `Configurator` instance. Example:

        >>> c = Configurator.load_config('vtservice.yaml', search_paths=['.'])

        :param file: Name of configuration file (with file extension included).
            Example: `'vtservice.yaml'`.
        :param search_paths: List of directory paths to be searched.
            Example: `['/etc/freemelt', '.']`
        :return: Instance of `Configurator`.
        """
        config_file = cls._find_config(file, search_paths)
        log.info('Found and will use configuration file: %s', config_file)
        config_dict = cls._load(config_file)
        log.info('Configuration file successfully loaded')
        return cls(config_dict)

    @staticmethod
    def _find_config(file, search_paths):
        """Search for configuration `file` in `search_paths`.

        :param file: Name of configuration file (with file extension included)
        :param search_paths: List of directory paths to be searched.
        :return: Path to file if found, `None` otherwise.
        """
        for path in search_paths:
            candidate = Path(path) / file
            if candidate.is_file():
                return candidate
        raise FileNotFoundError(f'File {file!r} not found in {search_paths!r}')

    @staticmethod
    def _load(file) -> dict:
        """Gets a dictionary representation of the given configuration `file`.

        YAML and JSON file types are supported.

        :param file: Yaml or json configuration file
        :return: Dictionary of configuration data
        """
        file = Path(file)
        with open(file, 'r') as cfg:
            if file.suffix in {'.yaml', '.yml'}:
                return yaml.safe_load(cfg)
            elif file.suffix == '.json':
                return json.load(cfg)
            else:
                raise ValueError(f'Loading configuration files of type '
                                 f'{file.suffix!r} is not implemented.')

    def __getitem__(self, key: str):
        """Get config data by specifying a "key1:key2:key3:..:keyN"-key.

        No type conversion will be done. The value will be returned untouched.
        (I.e the value will have the same type as written in the configuration
        file)

        Example:

        >>> # Create configurator
        >>> c = Configurator.load_config('vtservice.yaml', search_paths=['.'])
        >>> # Get value by ":"-separated key.
        >>> c['Config:OPC:Pressure:eGunPressure_GET']
        1.234
        >>> # You can also use the normal dictionary syntax if needed:
        >>> c['Config']['OPC']['Pressure']['eGunPressure_GET']
        1.234

        :param key: A key of the form "key1:key2:key3:..:keyN"
        :return: Config data value, corresponding to the N:th key of element.
        """
        keys = key.split(self.delimiter)
        output = functools.reduce(operator.getitem, keys, self.block)
        if isinstance(output, dict):
            return self.__class__(output, self.delimiter)
        return output

    def get(self, key: str, default=None):
        """Get config data by key or get default if key does not exist.

        No type conversion will be done. The value will be returned untouched.
        (I.e the value will have the same type as written in the configuration
        file)

        Example:

        >>> # Create configurator
        >>> c = Configurator.load_config('vtservice.yaml', search_paths=['.'])
        >>> # Get value by ":"-separated key. Default will be used if key does
        >>> # not exist in configuration file.
        >>> c.get('Config:VacuumService:Influx:Port', default=8086)
        8086

        If the type of the `default` value provided does not agree with the
        type according to the configuration file an exception will be raised.

        If no default value is not provided, it will not be used and the
        behaviour will be identical to `__getitem__`. I.e:

        >>> # Using .get without a default value:
        >>> c.get('Config:VacuumService:Influx:Port')
        >>> # Is the same as writing ths:
        >>> c['Config:VacuumService:Influx:Port']

        :param key: A key of the form "key1:key2:key3:..:keyN"
        :param default: A default value to return if the key does not exist.
        :return: Config data value, corresponding to the N:th key of element,
                 or default value.
        """
        if default is None:
            # Default not provided, behave as __getitem__.
            return self[key]
        try:
            value = self[key]
        except KeyError:
            log.debug('Key %s does not exist in configuration. '
                      'Default value will be used instead: %r', key, default)
            return default
        else:
            # Sanity check of type of default value
            if not isinstance(default, type(value)):
                raise TypeError(
                    f'The default value={default!r} of key={key!r} does not agree '
                    f'with the type of the value={value!r} ({type(value)})')
        return value

    def __str__(self):
        """Return a string of whole configuration dictionary"""
        return pformat(self.block)

    def get_str(self, key: str, default=None) -> str:
        """Return value as string.

        >>> config.get_str('Config:VacuumService:Influx:Database')
        'onelog'

        A default value can be provided in the same way as in the
        :meth:`Configurator.get` method.
        """
        value = self.get(key, default)
        return str(value)

    def get_bool(self, key: str, default=None) -> bool:
        """Return value as bool.

        >>> config.get_bool('Config:VacuumService:EnableSomething')
        True

        A default value can be provided in the same way as in the
        :meth:`Configurator.get` method.

        If the value specified in the configuration file is not a boolean,
        this method will try to convert the value into a boolean. For example,
        the strings "yes"/"true"/"on" will be interpreted as True and
        "no"/"false"/"off" will be interpreted as False. If the value can't be
        interpreted as a boolean, a TypeError with an explanation will be
        raised.
        """
        value = self.get(key, default)

        if isinstance(value, bool):
            return value
        elif isinstance(value, str):
            # Check if the string has a boolean meaning
            value = value.strip().lower()
            if value in {'yes', 'on', 'true', '1'}:
                return True
            elif value in {'no', 'off', 'false', '0'}:
                return False
        raise TypeError(f'Value {value!r} of key {key!r} could not be '
                        f'interpreted as a boolean!')

    def get_float(self, key: str, default=None) -> float:
        """Return value as float.

        >>> config.get_float('Config:Criteria:HighVacuumPumpStart_PressureMax')
        0.1

        A default value can be provided in the same way as in the
        :meth:`Configurator.get` method.

        If the value specified in the configuration file is not a float,
        this method will try to convert the value into a float. For example,
        the string "3.14" will be converted to 3.14. But the string "Pi" will
        fail. In case of failure, a TypeError with an explanation will be
        raised.
        """
        value = self.get(key, default)
        if isinstance(value, bool):
            # Actually, Python is happy converting a bool to float, for
            # example, float(True) == 1.0. This is probably a mistake in
            # the configuration file and should raise an error.
            raise TypeError(f'Value {value!r} of key {key!r} could not be '
                            f'interpreted as a float!')
        try:
            return float(value)
        except (ValueError, TypeError) as error:
            raise TypeError(f'Value {value!r} of key {key!r} could not be '
                            f'interpreted as a float!') from error

    def get_int(self, key: str, default=None) -> int:
        """Return value as int.

        >>> config.get_int('Config:VacuumService:Influx:Port')
        8086

        A default value can be provided in the same way as in the
        :meth:`Configurator.get` method.

        .. note:: It is an error to use get_int on a float if it implies that
                  precision will be lost. For example:
                  `get_int(3.0)` = OK and `get_int(3.14)` = FAIL.
        """
        value = self.get(key, default)
        try:
            f_value = float(value)
            i_value = int(value)
        except (ValueError, TypeError) as error:
            raise TypeError(f'Value {value!r} of key {key!r} could not be '
                            f'interpreted as a integer!') from error
        else:
            if f_value == i_value:
                return i_value
            raise TypeError(f'Value {value!r} of key {key!r} could not be '
                            f'interpreted as an integer without loosing '
                            f'precision.')
