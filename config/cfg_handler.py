""" cfg_handler.py: This module reads the configuration file and make the configuration params
                    for use for other modules """

import os
from configparser import ConfigParser


class CfgHandlerError(Exception):
    pass


class CfgHandler(ConfigParser, object):
    """
    CfgHandler handles all configuration related task; Reads
    the configuration file and make all configuration parameters
    available for use.
    """

    _defaultConfigFileName = "cfg.ini"
    _configFileInUse = None

    def __init__(self, cfg_file=None):
        """
        Constructor
        @param cfg_file: Configuration file path with name,
         if not provided then default is used: config/cfg.ini
        """
        super(CfgHandler, self).__init__()
        self.load_configuration(cfg_file)

    def load_configuration(self, cfg_file):
        """
        Load the configuration file in memory
        @raise CfgHandlerError: If configuration file cannot be loaded
        """
        self._configFileInUse = (os.path.abspath(os.path.dirname(__file__)) + os.sep +
                                 self._defaultConfigFileName) if cfg_file is None else cfg_file

        lst = self.read(self._configFileInUse)

        if len(lst) == 0:
            raise CfgHandlerError("Config file not found")

    def get_cfg_file_in_use(self):
        return self._configFileInUse
