# typing: Type Hints for Python

[![Build Status](https://travis-ci.org/JukkaL/typing.svg)](https://travis-ci.org/JukkaL/typing)

## What Is typing?

This is a backport of the `typing` module introduced in Python 3.5
beta 1 to Python 3.2, 3.3 and 3.4. The eventual goal is to also
provide a stripped-down implementation for Python 2.7. `typing` allows
you to add type annotations to your code in a standard format that
will be understood by static type checkers and IDEs.

Here is a small example:

```python
from typing import Iterator

def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
```

Documentation about `typing` in general is hosted everywhere (see the
links below).

## Status

This is work in progress. The `typing` module may still undergo small
changes before Python 3.5 is finalized.

The Python 2 version is woefully out of date.

## Useful Links

* https://www.python.org/dev/peps/pep-0484/: PEP 484 is a specification of the
  `typing` module.
* https://github.com/ambv/typehinting: Discussion about future improvements to
  `typing` happen here. If you want to contribute a new feature or fix that is
  not specific to pre-3.5 Python version, do it here.
* https://github.com/JukkaL/mypy: Mypy is a type checker that aims to conform
  to PEP 484.

## License

Since `typing` is lifted from Python 3.5, it's distributed under the
PSF license. The current Python 2 version (which does not conform to
PEP 484 yet) is distributed under the MIT license, but it will be
replaced by a version that is derived from the Python 3.5 version
soon.
