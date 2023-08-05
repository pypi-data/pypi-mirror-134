"""
Some useful extensions and protocols to standard typing library.
"""

import dataclasses
from typing import Protocol, ClassVar, Any, Dict, Type


class DataClass(Protocol):
    __dataclass_fields__: ClassVar[Dict[str, 'dataclasses.Field']]
    __dataclass_params__: ClassVar[Any]


class Missing:
    """
    A class to represent missing values when None is not an option that compares False (as empty values in Python)
    and brings a reference to the missing value itself, which could be a message or a type. Missing instances are
    considered equal if their references compares equal (via __eq__).
    """
    def __init__(self, ref: Any = None):
        self.ref = ref

    def __bool__(self):
        return False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.ref!r})@{hex(id(self))}"

    def __str__(self):
        return f"{self.__class__.__name__}({self.ref!s})"

    def __eq__(self, other):
        if isinstance(other, Missing):
            return self.ref == other.ref
        return NotImplemented


class Raise(Missing):
    def __init__(self, ref: Type[Exception | BaseException]):
        super().__init__(ref)

    def raise_exception(self, *args, **kwargs):
        raise self.ref(*args, **kwargs)

    def __call__(self):
        self.raise_exception()
