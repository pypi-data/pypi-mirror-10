u"""Static type checking helpers"""

from abc import ABCMeta, abstractmethod, abstractproperty
import collections
import inspect
import sys
import re
import functools


__all__ = [
    # Type system related
    'Any',
    'AnyStr',
    'Dict',
    'Callable',
    'Generic',
    'GenericMeta',
    'IO',
    'List',
    'Match',
    'NamedTuple',
    'Optional',
    'Pattern',
    'Set',
    'Tuple',
    'Undefined',
    'Union',
    'annotations',
    'cast',
    'overload',
    'TypeVar',
    # _Protocols and abstract base classes
    'Container',
    'Iterable',
    'Iterator',
    'Sequence',
    'Sized',
    'AbstractSet',
    'Mapping',
    'BinaryIO',
    'TextIO',
]


class GenericMeta(ABCMeta):
    """Metaclass for generic classes that support type indexing.

    This is used for ABCs and ordinary classes.
    """

    def __new__(mcls, name, bases, namespace):
        cls = ABCMeta.__new__(mcls, name, bases, namespace)
        # '_Protocol' must be an explicit base class in order for a class to
        # be a protocol.
        cls._is_protocol = name == u'_Protocol' or _Protocol in bases
        return cls

    def __getitem__(self, args):
        # Just ignore args; they are for compile-time checks only.
        return self


class _Protocol(object):
    __metaclass__ = GenericMeta
    """Base class for protocol classes."""

    @classmethod
    def __subclasshook__(cls, c):
        if not cls._is_protocol:
            # No structural checks since this isn't a protocol.
            return NotImplemented

        if cls is _Protocol:
            # Every class is a subclass of the empty protocol.
            return True

        # Find all attributes defined in the protocol.
        attrs = cls._get_protocol_attrs()

        for attr in attrs:
            if not any(attr in d.__dict__ for d in c.__mro__):
                return NotImplemented
        return True

    @classmethod
    def _get_protocol_attrs(cls):
        # Get all _Protocol base classes.
        protocol_bases = []
        for c in cls.__mro__:
            if getattr(c, '_is_protocol', False) and c.__name__ != '_Protocol':
                protocol_bases.append(c)

        # Get attributes included in protocol.
        attrs = set()
        for base in protocol_bases:
            for attr in base.__dict__.keys():
                # Include attributes not defined in any non-protocol bases.
                for c in cls.__mro__:
                    if (c is not base and attr in c.__dict__ and
                            not getattr(c, '_is_protocol', False)):
                        break
                else:
                    if (not attr.startswith(u'_abc_') and
                        attr != '__abstractmethods__' and
                        attr != '_is_protocol' and
                        attr != '__dict__' and
                        attr != '_get_protocol_attrs' and
                        attr != '__module__'):
                        attrs.add(attr)

        return attrs


class Generic(object):
    __metaclass__ = GenericMeta
    """Base class for (abstract) generic classes."""


class TypeAlias(object):
    """Class for defining generic aliases for library types."""

    def __init__(self, target_type):
        self.target_type = target_type

    def __getitem__(self, typeargs):
        return self.target_type


# Define aliases for built-in types that support indexing.
List = TypeAlias(list)
Dict = TypeAlias(dict)
Set = TypeAlias(set)
Tuple = TypeAlias(tuple)
Callable = TypeAlias(callable)
Pattern = TypeAlias(type(re.compile('')))
Match = TypeAlias(type(re.match('', '')))


def union(x): return x


Union = TypeAlias(union)


class _Optional:
    def __getitem__(self, typearg):
        return Union[typearg, None]


Optional = _Optional()


def NamedTuple(typename, fields):
    return collections.namedtuple(typename,
                                  (name for name, type in fields))


class TypeVar(object):
    def __init__(self, name, *values):
        self.name = name
        if not values:
            values = None
        self.values = values


# Predefined type variables.
AnyStr = TypeVar('AnyStr', str, unicode)


def Any(x):
    """The Any type; can also be used to cast a value to type Any."""
    return x


def cast(type, object):
    """Cast a value to a type.

    This only affects static checking; simply return object at runtime.
    """
    return object


def annotations(**kwargs):
    """Add Python 3 style __annotations__ to a Python 2 function.

    The return annotation should be specified via the 'returns' keyword
    argument to be syntactically valid.
    """
    def wrapper(func):
        if 'returns' in kwargs:
            kwargs['return'] = kwargs.pop('returns')
        func.__annotations__ = kwargs
        return func
    return wrapper


def overload(func):
    raise RuntimeError("Overloading only supported in library stubs")


class Undefined(object):
    """Class that represents an undefined value with a specified type.

    At runtime the name Undefined is bound to an instance of this
    class.  The intent is that any operation on an Undefined object
    raises an exception, including use in a boolean context.  Some
    operations cannot be disallowed: Undefined can be used as an
    operand of 'is', and it can be assigned to variables and stored in
    containers.

    'Undefined' makes it possible to declare the static type of a
    variable even if there is no useful default value to initialize it
    with:

      from typing import Undefined
      x = Undefined(int)
      y = Undefined # type: int

    The latter form can be used if efficiency is of utmost importance,
    since it saves a call operation and potentially additional
    operations needed to evaluate a type expression.  Undefined(x)
    just evaluates to Undefined, ignoring the argument value.
    """

    def __repr__(self):
        return '<typing.Undefined>'

    def __setattr__(self, attr, value):
        raise AttributeError("'Undefined' object has no attribute '%s'" % attr)

    def __eq__(self, other):
        raise TypeError("'Undefined' object cannot be compared")

    def __ne__(self, other):
        raise TypeError("'Undefined' object cannot be compared")

    def __call__(self, type):
        return self

    def __nonzero__(self):
        raise TypeError("'Undefined' object is not valid as a boolean")

    def __hash__(self):
        raise TypeError("'Undefined' object is not hashable")


Undefined = Undefined()


# Abstract classes


T = TypeVar('T')
KT = TypeVar('KT')
VT = TypeVar('VT')


class SupportsInt(_Protocol):
    @abstractmethod
    def __int__(self): pass


class SupportsFloat(_Protocol):
    @abstractmethod
    def __float__(self): pass


class SupportsAbs(_Protocol[T]):
    @abstractmethod
    def __abs__(self): pass


class Reversible(_Protocol[T]):
    @abstractmethod
    def __reversed__(self): pass


class Sized(_Protocol):
    @abstractmethod
    def __len__(self): pass


class Container(_Protocol[T]):
    @abstractmethod
    def __contains__(self, x): pass


class Iterable(_Protocol[T]):
    @abstractmethod
    def __iter__(self): pass


class Iterator(Iterable[T], _Protocol[T]):
    @abstractmethod
    def next(self): pass


class Sequence(Sized, Iterable[T], Container[T], Generic[T]):
    @abstractmethod
    def __getitem__(self, i): pass

    @abstractmethod
    def __getitem__(self, s): pass

    @abstractmethod
    def __reversed__(self, s): pass

    @abstractmethod
    def index(self, x): pass

    @abstractmethod
    def count(self, x): pass


for t in list, tuple, unicode, str, xrange:
    Sequence.register(t)


class AbstractSet(Sized, Iterable[T], Generic[T]):
    @abstractmethod
    def __contains__(self, x): pass
    @abstractmethod
    def __and__(self, s): pass
    @abstractmethod
    def __or__(self, s): pass
    @abstractmethod
    def __sub__(self, s): pass
    @abstractmethod
    def __xor__(self, s): pass
    @abstractmethod
    def isdisjoint(self, s): pass


for t in set, frozenset, type({}.keys()), type({}.items()):
    AbstractSet.register(t)


class Mapping(Sized, Iterable[KT], Generic[KT, VT]):
    @abstractmethod
    def __getitem__(self, k): pass
    @abstractmethod
    def __setitem__(self, k, v): pass
    @abstractmethod
    def __delitem__(self, v): pass
    @abstractmethod
    def __contains__(self, o): pass

    @abstractmethod
    def clear(self): pass
    @abstractmethod
    def copy(self): pass
    @abstractmethod
    def get(self, k): pass
    @abstractmethod
    def get(self, k, default): pass
    @abstractmethod
    def pop(self, k): pass
    @abstractmethod
    def pop(self, k, default): pass
    @abstractmethod
    def popitem(self): pass
    @abstractmethod
    def setdefault(self, k): pass
    @abstractmethod
    def setdefault(self, k, default): pass

    @abstractmethod
    def update(self, m): pass
    @abstractmethod
    def update(self, m): pass

    @abstractmethod
    def keys(self): pass
    @abstractmethod
    def values(self): pass
    @abstractmethod
    def items(self): pass


# TODO Consider more types: os.environ, etc. However, these add dependencies.
Mapping.register(dict)


# Note that the BinaryIO and TextIO classes must be in sync with typing module stubs.


class IO(Generic[AnyStr]):
    @abstractproperty
    def mode(self): pass
    @abstractproperty
    def name(self): pass
    @abstractmethod
    def close(self): pass
    @abstractmethod
    def closed(self): pass
    @abstractmethod
    def fileno(self): pass
    @abstractmethod
    def flush(self): pass
    @abstractmethod
    def isatty(self): pass
    @abstractmethod
    def read(self, n=-1): pass
    @abstractmethod
    def readable(self): pass
    @abstractmethod
    def readline(self, limit=-1): pass
    @abstractmethod
    def readlines(self, hint=-1): pass
    @abstractmethod
    def seek(self, offset, whence=0): pass
    @abstractmethod
    def seekable(self): pass
    @abstractmethod
    def tell(self): pass
    @abstractmethod
    def truncate(self, size=None): pass
    @abstractmethod
    def writable(self): pass
    @abstractmethod
    def write(self, s): pass
    @abstractmethod
    def writelines(self, lines): pass

    @abstractmethod
    def __enter__(self): pass
    @abstractmethod
    def __exit__(self, type, value, traceback): pass


class BinaryIO(IO[str]):
    @abstractmethod
    def write(self, s): pass
    @abstractmethod
    def __enter__(self): pass


class TextIO(IO[unicode]):
    @abstractproperty
    def buffer(self): pass
    @abstractproperty
    def encoding(self): pass
    @abstractproperty
    def errors(self): pass
    @abstractproperty
    def line_buffering(self): pass
    @abstractproperty
    def newlines(self): pass
    @abstractmethod
    def __enter__(self): pass


# TODO Register TextIO/BinaryIO as the base class of file-like types.


del t
