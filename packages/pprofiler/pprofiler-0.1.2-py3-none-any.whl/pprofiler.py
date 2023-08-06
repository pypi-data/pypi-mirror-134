import cProfile, pstats
from functools import wraps, partial


def parameterized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)

        return repl

    return layer


@parameterized
def pprof(f, sort_by="ncalls", line_to_print=None, strip_dirs=False):
    @wraps(f)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = f(*args, **kwargs)
        profiler.disable()
        print_stats(profiler, sort_by=sort_by, line_to_print=None, strip_dirs=strip_dirs)
        return result

    return wrapper


def print_stats(profiler, sort_by="ncalls", line_to_print=None, strip_dirs=False):
    stats = pstats.Stats(profiler)
    if strip_dirs:
        stats.strip_dirs()

    if isinstance(sort_by, (tuple, list)):
        stats.sort_stats(*sort_by)
    else:
        stats.sort_stats(sort_by)
    stats.print_stats(line_to_print)
