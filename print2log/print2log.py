import builtins
import logging
from contextlib import contextmanager
from functools import lru_cache


@lru_cache()
def set_up_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(filename)s:%(lineno)d | %(message)s ",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger(__name__)


def print_as_log(*args, **kwargs):
    logger = set_up_logger()
    logger.info(*args, **kwargs)


@contextmanager
def log2print():
    original = builtins.print

    try:
        builtins.print = print_as_log
        yield
    finally:
        builtins.print = original


builtins.print = print_as_log

if __name__ == "__main__":
    with log2print():
        print(f"This is a log line from module: {__name__}")
