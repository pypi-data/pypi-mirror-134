from functools import wraps

from .utils import create_logger

handlers = []
handler_logger = create_logger('handlers')


def on(type: str, **on_args):
    def inner(func):
        handler_configuration = dict(type=type,
                                     configurations=on_args,
                                     handler=func)

        handlers.append(handler_configuration)
        handler_logger.info(f'register handler: {handler_configuration}')

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return inner
