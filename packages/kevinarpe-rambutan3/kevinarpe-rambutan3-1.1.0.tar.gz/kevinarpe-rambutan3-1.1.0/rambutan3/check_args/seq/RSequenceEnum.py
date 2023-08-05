from _collections_abc import Sequence, MutableSequence

from rambutan3.enumeration.REnum import REnum


class RSequenceEnum(REnum):

    TUPLE = (tuple,)
    LIST = (list,)
    SEQUENCE = (tuple, Sequence, list, MutableSequence)
