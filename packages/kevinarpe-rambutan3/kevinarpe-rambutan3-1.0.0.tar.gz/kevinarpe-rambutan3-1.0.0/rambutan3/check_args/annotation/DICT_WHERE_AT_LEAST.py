from rambutan3.check_args.dict.RDictEnum import RDictEnum
from rambutan3.check_args.dict.RDictWhereMatcher import RDictWhereMatcher


def DICT_WHERE_AT_LEAST(matcher_dict: dict) -> RDictWhereMatcher:
    x = RDictWhereMatcher(RDictEnum.DICT, matcher_dict, is_exact=False)
    return x
