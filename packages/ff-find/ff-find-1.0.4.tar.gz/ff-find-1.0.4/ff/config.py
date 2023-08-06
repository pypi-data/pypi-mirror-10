# -*- coding: utf-8 -*-

"""
Read and parse configuration files
"""

try:
    import configparser
except ImportError:
    import ConfigParser as configparser
import os, os.path

from ff import scanner
from ff import utils


class ConfigError(Exception):
    """ Configuration file error
    """
    pass


class FFConfigParser(configparser.ConfigParser):
    ''' Extended version of ConfigParser: strip quotes from values
    '''
    def get(self, *a, **b):
        ''' Override ConfigParser.get and for string values strip surrounding quotes
        '''
        val = configparser.ConfigParser.get(self, *a, **b)

        if not utils.IS_PY2:
            if isinstance(val, str):
                val = self.strip_quotes(val)
        else:
            if isinstance(val, (str, unicode)):
                val = self.strip_quotes(val)

        return val

    @staticmethod
    def strip_quotes(value):
        """
        If value surrounds single or double quotes, strip them
        :param value:str
        :return:str
        """
        if value[0] == '"' and value[-1] == '"':
            value = value[1:-1]
        elif value[0] == "'" and value[-1] == "'":
            value = value[1:-1]

        return value


# pylint: disable=too-many-instance-attributes,too-few-public-methods
class Config(object):
    """
    Configuration of ff
    """
    def __init__(self):
        self.ignorecase = False
        self.smartcase = False
        self.print0 = False
        self.depth = -1
        self.mode = scanner.MODE_ALL
        self.regexp = False
        self.fuzzy = False
        self.path_search = False
        self.prefix = False
        self.prefix_dirs = 'd: '
        self.prefix_files = 'f: '
        self.colorize = True
        self.include_vcs = False

        self.excluded_paths = []
        self.plugins_paths = []

    def __str__(self):
        ret = []

        items = (
            'ignorecase', 'smartcase', 'print0', 'regexp', 'fuzzy',
            'path_search', 'prefix', 'colorize', 'include_vcs',
        )
        for item in items:
            if getattr(self, item):
                ret.append(item)

        items = ('depth', 'mode', 'prefix_dirs', 'prefix_files')
        for item in items:
            ret.append('%s="%s"' % (item, getattr(self, item)))

        ret.sort()

        if self.plugins_paths:
            ret.append('plugins_paths:cnt:%d' % len(self.plugins_paths))

        if self.excluded_paths:
            ret.append('excluded_paths:cnt:%d' % len(self.excluded_paths))

        return 'Config(%s)' % ','.join(ret)


    # pylint: disable=too-many-branches
    @classmethod
    def parse_config(cls, sources=None):
        """
        Parse files, initialize Config instance and fill them with data
        :param sources:[str]
        :return:Config
        """
        if not sources:
            sources = [
                os.path.join(os.path.expanduser('~'), '.ff.rc'),
                os.path.join(utils.getcwd(), '.ff.rc')
            ]

        self = cls()

        try:
            parser = FFConfigParser()
            parser.read(sources)
        except configparser.ParsingError as ex:
            raise ConfigError(str(ex))

        if parser.sections() and not parser.has_section('ff'):
            raise ConfigError("Missing 'ff' section in config file")

        if parser.has_option('ff', 'ignorecase'):
            self.ignorecase = parser.getboolean('ff', 'ignorecase')
        if parser.has_option('ff', 'smartcase'):
            self.smartcase = parser.getboolean('ff', 'smartcase')
        if parser.has_option('ff', 'print0'):
            self.print0 = parser.getboolean('ff', 'print0')
        if parser.has_option('ff', 'depth'):
            self.depth = parser.getint('ff', 'depth')
        if parser.has_option('ff', 'mode'):
            self.mode = parser.get('ff', 'mode')
        if parser.has_option('ff', 'regexp'):
            self.regexp = parser.getboolean('ff', 'regexp')
        if parser.has_option('ff', 'fuzzy'):
            self.fuzzy = parser.getboolean('ff', 'fuzzy')
        if parser.has_option('ff', 'path_search'):
            self.path_search = parser.getboolean('ff', 'path_search')
        if parser.has_option('ff', 'prefix'):
            self.prefix = parser.getboolean('ff', 'prefix')
        if parser.has_option('ff', 'prefix_dirs'):
            self.prefix_dirs = parser.get('ff', 'prefix_dirs')
        if parser.has_option('ff', 'prefix_files'):
            self.prefix_files = parser.get('ff', 'prefix_files')
        if parser.has_option('ff', 'colorize'):
            self.colorize = parser.getboolean('ff', 'colorize')
        if parser.has_option('ff', 'include_vcs'):
            self.include_vcs = parser.getboolean('ff', 'include_vcs')

        if parser.has_section('excluded_paths'):
            for item in parser.options('excluded_paths'):
                enabled = parser.getboolean('excluded_paths', item)
                if enabled:
                    self.excluded_paths.append(item)

        if parser.has_section('plugins_paths'):
            for item in parser.options('plugins_paths'):
                enabled = parser.getboolean('plugins_paths', item)
                if enabled:
                    self.plugins_paths.append(item)

        return self
