import logging
import sys
import uuid


def create_logger(name) -> logging.Logger:
    log_level = logging.INFO

    log = logging.getLogger(name)
    log.setLevel(log_level)
    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log

def is_valid_uuid4(value):
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False
