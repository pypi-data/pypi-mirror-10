import signal
import functools


class TimeoutError(Exception):
    pass


def timeout(seconds, error_message='Function call timed out'):
    """
    https://wiki.python.org/moin/PythonDecoratorLibrary

    import time

    @timeout(1, 'Function slow; aborted')
    def slow_function():
        time.sleep(5)
    """
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wrappe

    return decorated
