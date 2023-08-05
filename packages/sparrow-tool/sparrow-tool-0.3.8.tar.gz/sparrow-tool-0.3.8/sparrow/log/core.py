import colorlog
import logging
from concurrent_log_handler import ConcurrentRotatingFileHandler
import os
import inspect
from pathlib import Path
from functools import wraps
import datetime
from ..decorators.core import MetaSingleton


class Logger(metaclass=MetaSingleton):
    def __init__(self,
                 log_dir='./',
                 debug_path="debug.log",
                 info_path='info.log',
                 warning_path='warn.log',
                 error_path='error.log',
                 print_debug=False,
                 print_info=False,
                 print_warning=False,
                 print_error=False,
                 single_mode=False,
                 level=logging.DEBUG,
                 tz='origin'
                 ):
        """
        Parameters
        ----------
            tz: time zone, to point china time zone you can use options: 'zh','ch','shanghai','beijing'。
        """
        self.colors_config = {
            'DEBUG': 'white',
            'INFO': 'cyan',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }

        if tz.lower() in ("zh", "ch", "shanghai", 'beijing'):
            logging.Formatter.converter = lambda sec, what: \
                (datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=8)).timetuple()
        debug_path = Path(log_dir).joinpath(debug_path)
        info_path = Path(log_dir).joinpath(info_path)
        warning_path = Path(log_dir).joinpath(warning_path)
        error_path = Path(log_dir).joinpath(error_path)
        self._debug_logger = self._get_logger("debug-inner-name", debug_path, level=logging.DEBUG, stream=print_debug)
        self._info_logger = self._get_logger("info-inner-name", info_path, level=logging.INFO, stream=print_info)
        self._warining_logger = self._get_logger("warning-inner-name", warning_path, level=logging.WARNING,
                                                 stream=print_warning)
        self._error_logger = self._get_logger("error-inner-name", error_path, level=logging.ERROR, stream=print_error)
        self._single_mode = single_mode
        self._level = level

    @classmethod
    def getLogger(cls):
        """Logger is singleton，this is equivalent to using Logger () directly"""
        return cls()

    def debug(self, msg, *args, **kwargs):
        currentframe = inspect.currentframe()
        msg = self.get_format_msg(currentframe, msg, "DEBUG")
        if self._level <= logging.DEBUG:
            self._debug_logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        currentframe = inspect.currentframe()
        msg = self.get_format_msg(currentframe, msg, "INFO")
        if self._level <= logging.INFO:
            self._info_logger.info(msg, *args, **kwargs)
            if not self._single_mode:
                self._debug_logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        currentframe = inspect.currentframe()
        msg = self.get_format_msg(currentframe, msg, "WARNING")
        if self._level <= logging.WARNING:
            self._warining_logger.warning(msg, *args, **kwargs)
            if not self._single_mode:
                self._debug_logger.warning(msg, *args, **kwargs)
                self._info_logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        currentframe = inspect.currentframe()
        msg = self.get_format_msg(currentframe, msg, "ERROR")
        if self._level <= logging.ERROR:
            self._error_logger.error(msg, *args, **kwargs)
            if not self._single_mode:
                self._debug_logger.error(msg, *args, **kwargs)
                self._info_logger.error(msg, *args, **kwargs)
                self._warining_logger.error(msg, *args, **kwargs)

    @staticmethod
    def get_format_msg(currentframe, msg, level):
        filename = os.path.basename(currentframe.f_back.f_code.co_filename)
        lineno = currentframe.f_back.f_lineno
        msg = f"[{filename}]-[line:{lineno}]-{level} >>> " + str(msg)
        return msg

    def _get_logger(self, name, log_abs_path, level=logging.INFO, stream=True):
        default_formats = {
            'color_format': '%(log_color)s%(asctime)s-%(message)s',
            'log_format': '%(asctime)s-%(message)s'
        }
        # default_formats = {
        #     'color_format': '%(log_color)s%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]-%(levelname)s: %('
        #                     'message)s',
        #     'log_format': f'%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]-%(levelname)s: %(message)s'
        # }

        log_path = Path(log_abs_path).absolute()
        log_dir = log_path.parent
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        logger = logging.getLogger(name)

        stream_formatter = colorlog.ColoredFormatter(default_formats["color_format"],
                                                     log_colors=self.colors_config,
                                                     datefmt='%Y/%m/%d %H:%M:%S')

        file_formatter = logging.Formatter(default_formats["log_format"],
                                           datefmt='%Y-%m-%d %H:%M:%S')

        file_handler = ConcurrentRotatingFileHandler(filename=log_path,
                                                     maxBytes=10 * 1024 * 1024,
                                                     backupCount=10,
                                                     encoding='utf-8')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        if stream:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(stream_formatter)
            logger.addHandler(stream_handler)
        logger.setLevel(level)

        return logger


# unused.
def findcaller(func):
    @wraps(func)
    def wrapper(*args):
        currentframe = inspect.currentframe()
        f = currentframe.f_back
        file_name = os.path.basename(f.f_code.co_filename)
        func_name = f.f_code.co_name
        line_num = f.f_lineno

        args = list(args)
        args.append(f'{os.path.basename(file_name)}.{func_name}.{line_num}')
        func(*args)

    return wrapper
