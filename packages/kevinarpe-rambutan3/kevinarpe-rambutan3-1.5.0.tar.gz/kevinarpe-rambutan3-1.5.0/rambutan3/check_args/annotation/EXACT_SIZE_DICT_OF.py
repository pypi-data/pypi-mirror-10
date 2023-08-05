from rambutan3.check_args.base.RAbstractTypeMatcher import RAbstractTypeMatcher
from rambutan3.check_args.dict.RDictEnum import RDictEnum
from rambutan3.check_args.dict.RRangeSizeDictOfMatcher import RRangeSizeDictOfMatcher
from rambutan3.check_args.seq.RRangeSizeSequenceOfMatcher import RRangeSizeSequenceOfMatcher
from rambutan3.check_args.seq.RSequenceEnum import RSequenceEnum


# noinspection PyPep8Naming
def EXACT_SIZE_DICT_OF(*,
                       key_matcher: RAbstractTypeMatcher=None,
                       type_matcher: RAbstractTypeMatcher=None,
                       exact_size: int) -> RRangeSizeDictOfMatcher:

    x = RRangeSizeDictOfMatcher(RDictEnum.DICT,
                                key_matcher=key_matcher,
                                value_matcher=type_matcher,
                                min_size=exact_size,
                                max_size=exact_size)
    return x
