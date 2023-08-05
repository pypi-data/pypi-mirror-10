from rambutan3.check_args.base.RAbstractTypeMatcher import RAbstractTypeMatcher
from rambutan3.check_args.set.RSetEnum import RSetEnum
from rambutan3.check_args.set.RSetOfMatcher import RSetOfMatcher


def SET_OF(type_matcher: RAbstractTypeMatcher) -> RSetOfMatcher:
    x = RSetOfMatcher(RSetEnum.SET, type_matcher)
    return x