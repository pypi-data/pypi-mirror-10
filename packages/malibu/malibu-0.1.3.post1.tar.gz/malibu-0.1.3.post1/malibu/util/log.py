import logging, malibu

from logging import handlers

from malibu.config import configuration
from malibu.util import get_caller

class LoggingDriver(object):

    __instances = {}

    @classmethod
    def get_instance(cls, name = None):

        if name is None:
            # Assume that we are using the logger driver that was built for 
            # this package.
            name = get_caller().split('.')[0]
        
        if not cls.__instances or name not in cls.__instances:
            return None

        return cls.__instances[name]

    @classmethod
    def get_logger(cls, name = None):

        if name is None:
            name = get_caller()
            root = name.split('.')[0]

        if not cls.get_instance(name = root):
            return None
        
        return cls.get_instance(name = root).get_logger(name = name)
    
    def __init__(self, config = {}, name = None):
        """ __init__(self, config = {}, name = None)

            Initializes the logging driver and loads necessary config
            values from the ConfigurationSection that should be passed
            in as config. Also loads the root logger from a specified
            default name or from the base module name of the package.
        """

        if not isinstance(config, configuration.ConfigurationSection):
            raise TypeError("Config should be of type "
                    "malibu.config.configuration.ConfigurationSection.")
        
        self.__config = config

        if not name:
            self.name = get_caller().split('.')[0]

        self.__logfile = self.__config.get_string("logfile", 
                "/var/log/{}.log".format(self.name))
        self.__loglevel = self.__config.get_string("loglevel", "INFO").upper()
        self.__stream = self.__config.get_bool("console_log", True)

        self.__loglevel = getattr(logging, self.__loglevel, None)
        if not isinstance(self.__loglevel, int):
            raise TypeError("Invalid log level: {}".format(
                self.__config.get_string("loglevel", "INFO").upper()))

        LoggingDriver.__instances[self.name] = self

        self.__setup_logger()

    def __setup_logger(self):
        """ __setup_logger(self)

            Sets up the logging system with the logfile, loglevel, and
            other streaming options.
        """

        # Set up logging with the root handler so all log objects get the same
        # configuration.
        logger = logging.getLogger(self.name)
        logger.setLevel(self.__loglevel)
        formatter = logging.Formatter('%(asctime)s | %(name)-50s %(levelname)s : %(message)s')

        file_logger = handlers.RotatingFileHandler(
                self.__logfile,
                maxBytes = 8388608, # 8MB
                backupCount = 4)
        file_logger.setLevel(self.__loglevel)
        file_logger.setFormatter(formatter)

        logger.addHandler(file_logger)

        if self.__stream:
            logger.debug(" --> Building streaming log handler...")
            stream_logger = logging.StreamHandler()
            stream_logger.setLevel(self.__loglevel)
            stream_logger.setFormatter(formatter)

            logger.addHandler(stream_logger)

        logger.info(" --> Logfile is opened at: {}".format(self.__logfile))

    def get_logger(self, name = None):
        """ get_logger(self, name = None)

            Will return a logger object for a specific namespace. 
            If name parameter is None, get_logger will use call
            stack inspection to get the namespace of the last caller.
        """

        if name is None:
            name = get_caller()

        return logging.getLogger(name)
