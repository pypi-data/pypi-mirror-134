from attrs import define, field, validators


class _SentinelBase(type):
    """
    Sentinel values

     - Inherit identity-based comparison and hashing from object
     - Have a nice repr
     - Have a *bonus property*: type(sentinel) is sentinel

     The bonus property is useful if you want to take the return value from
     next_event() and do some sort of dispatch based on type(event).

     Taken from h11.
    """

    def __repr__(self):
        return self.__name__


def make_sentinel(name):
    cls = _SentinelBase(name, (_SentinelBase,), {})
    cls.__class__ = cls
    return cls


NOT_CONNECTED = make_sentinel("NOT_CONNECTED")


@define
class ElgasState:
    ...
