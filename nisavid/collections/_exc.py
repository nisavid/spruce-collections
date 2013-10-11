"""Exceptions."""

__copyright__ = "Copyright (C) 2013 Ivan D Vasin and Cogo Labs"
__docformat__ = "restructuredtext"


class Error(RuntimeError):
    pass


class UnsupportedUniversalSetOperation(Error):

    """
    A finite set operation was attempted on a universal set.

    :param operation:
        The attempted operation.
    :type operation: :obj:`str`

    :param message:
        A message that describes the error.
    :type message: :obj:`str` or null

    """

    def __init__(self, operation, set, message=None, *args):
        self._message = message
        self._operation = operation
        self._set = set
        super(UnsupportedUniversalSetOperation, self)\
         .__init__(operation, set, message, *args)

    def __str__(self):
        message = '{} is unsupported by the universal set {!r}'\
                   .format(self.operation, self.set)
        if self.message:
            message += ': ' + self.message
        return message

    @property
    def message(self):
        return self._message

    @property
    def operation(self):
        return self._operation

    @property
    def set(self):
        return self._set
