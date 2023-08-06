import sys
import time
from contextlib import ContextDecorator


class timeit(ContextDecorator):
    def __init__(self, tag: str = '-'):
        self.tag = tag

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start

        if duration < 1:
            formatted = f'{round(duration * 1000, 8)} ms'
        elif duration < 60:
            formatted = f'{round(duration, 8)} s'
        else:
            formatted = f'{round(duration / 60, 8)} m'

        sys.stdout.write(f'EXECUTION TIME :: {self.tag} :: {formatted}\n')
        return False
