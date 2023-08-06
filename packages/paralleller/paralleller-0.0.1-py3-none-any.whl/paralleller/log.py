import logging
import time
import os


def get_logger(name, log_level=logging.DEBUG):
    """一般日志设置所采用的方式"""
    log = logging.getLogger(name)
    log.setLevel(log_level)
    directory = os.path.join('log', time.strftime('%Y%m%d-%H%M%S'))
    if not os.path.isdir(directory):
        os.makedirs(directory, exist_ok=True)
    filename = os.path.join(directory, '{}.log'.format(name))
    fh = logging.FileHandler(filename)
    formatter = logging.Formatter('%(asctime)s - %(processName)s - '
                                  '%(threadName)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    log.addHandler(fh)
    return log
