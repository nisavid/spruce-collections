"""Miscellaneous set data types."""

__copyright__ = "Copyright (C) 2013 Ivan D Vasin and Cogo Labs"
__docformat__ = "restructuredtext"

import __builtin__
import oset as _oset


class set(__builtin__.set):

    """A set.

    .. seealso:: :class:`set <python:set>`

    """

    def __repr__(self):
        return '{{{}}}'.format(', '.join(repr(item) for item in self)) \
               if self else 'set()'

    def __str__(self):
        return '{{{}}}'.format(', '.join(str(item) for item in self)) \
               if self else 'set()'


class frozenset(__builtin__.frozenset):

    """An immutable set.

    .. seealso:: :class:`frozenset <python:frozenset>`

    """

    def __repr__(self):
        return '={{{}}}'.format(', '.join(repr(item) for item in self))

    def __str__(self):
        return '={{{}}}'.format(', '.join(str(item) for item in self))


class oset(_oset.oset):

    """An ordered set.

    .. seealso:: :mod:`oset` from :pypi:`oset`

    """

    def __repr__(self):
        return '{}({!r})'.format(self.__class__.__name__,
                                 [item for item in self])

    def __str__(self):
        return '>{{{}}}'.format(', '.join(str(item) for item in self))
