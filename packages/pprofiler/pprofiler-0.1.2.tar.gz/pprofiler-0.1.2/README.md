# pprofiler

Simple Python Decorator to Profiling Function or Method

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pprofiler.

```bash
pip install pprofiler
```

## Usage


```
Python 3.8.10 (default, Jun 23 2021, 11:56:21)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.24.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from pprofiler import pprof

In [2]: @pprof(sort_by=["cumulative", "ncalls"])
   ...: def test():
   ...:     arr = []
   ...:     for i in range(0, 100_000):
   ...:         arr.append(i)
   ...:

In [3]: test()
         100002 function calls in 0.018 seconds

   Ordered by: cumulative time, call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.012    0.012    0.018    0.018 <ipython-input-4-87325251511f>:1(test)
   100000    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```


# pprofiler 0.1.2 Release Notes
## January 12, 2022

## Changelog

* Add `line_to_print` parameter - to reduce output for large profiler output
* Add `strip_dirs` parameter - to reduce output for large profiler output
* `sort_by` parameter now accept `tuple` or `list`


## License
[MIT](https://choosealicense.com/licenses/mit/)
