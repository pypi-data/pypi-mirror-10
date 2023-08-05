import os
import asyncio
from collections import OrderedDict
from configparser import ConfigParser, ExtendedInterpolation

# from aio.core.exceptions import MissingConfiguration


def gather_config(modules, filename=None):
    config_files = []
    for module in modules:
        path = module.__path__[0]
        app_config = os.path.join(path, filename or "aio.conf")
        if os.path.exists(app_config):
            config_files.append(app_config)
    return config_files


def find_config(app_dir=None, filename=None):
    if not app_dir:
        app_dir = os.getcwd()
    config = os.path.join(app_dir, filename or 'aio.conf')
    if os.path.exists(config):
        return config
    config = os.path.join(app_dir, 'etc', filename or 'aio.conf')
    if os.path.exists(config):
        return config
    config = os.path.join(app_dir, '/etc', filename or 'aio.conf')
    if os.path.exists(config):
        return config
    # raise MissingConfiguration('no configuration file found')


@asyncio.coroutine
def parse_config(config=None, config_files=None, app_dir=None,
                 config_dict=None, config_string=None,
                 modules=None, parser=None, interpolation=None,
                 filename=None):
    parser = parser or ConfigParser(
        interpolation=interpolation or ExtendedInterpolation())
    if config_dict:
        parser.read_dict(config_dict)
    elif config_string:
        parser.read_string(config_string)
    elif config_files:
        for config_file in config_files:
            parser.read_file(open(config))
    elif modules:
        for config_file in gather_config(modules, filename=filename):
            parser.read_file(open(config_file))
    else:
        config = config or find_config(app_dir, filename=filename)
        if config:
            parser.read_file(open(config))
    return parser


class ConfigSection(OrderedDict):

    pass


class Config(OrderedDict):

    pass


def replicate_config(config, test_section=None):
    new_config = Config()
    for section_name, section in config.items():
        if test_section:
            if not test_section(section_name):
                continue
        new_config[section_name] = ConfigSection()
        for option_name, option in section.items():
            new_config[section_name][option_name] = option
    return new_config
