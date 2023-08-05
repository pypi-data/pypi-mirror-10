from rambutan3 import RArgs
from rambutan3.check_args.base.RAbstractTypeMatcher import RAbstractTypeMatcher


RInstanceMatcher = None


# noinspection PyRedeclaration
class RInstanceMatcher(RAbstractTypeMatcher):
    """Type instance matcher

    Example: {@code "abc"} has type {@link str}
    Example: {@code 123.456} has type {@link float}

    This class is fully tested.

    @author Kevin Connor ARPE (kevinarpe@gmail.com)

    @see builtins#isinstance()
    """

    def __init__(self, *class_or_type_tuple):
        """
        @param *class_or_type_tuple
               one or more value type classes, e.g., {@link str} or {@link float}

        @throws ValueError
                if {@code *class_or_type_tuple} is empty
        @throws TypeError
                if {@code *class_or_type_tuple} contains a item that is not a type/class
        """
        super().__init__()
        RArgs.check_iterable_not_empty_and_items_is_instance(class_or_type_tuple, type, "*class_or_type_tuple")
        self.__type_tuple = class_or_type_tuple
        self.__type_frozenset = frozenset(class_or_type_tuple)

    # @override
    def matches(self, value) -> bool:
        x = isinstance(value, self.__type_tuple)
        return x

    # @override
    def __eq__(self, other: RInstanceMatcher) -> bool:
        if not isinstance(other, RInstanceMatcher):
            return False
        x = (self.__type_frozenset == other.__type_frozenset)
        return x

    # @override
    def __hash__(self) -> int:
        x = hash(self.__type_frozenset)
        return x

    # @override
    def __str__(self) -> str:
        x = " | ".join([x.__name__ for x in self.__type_tuple])
        return x
