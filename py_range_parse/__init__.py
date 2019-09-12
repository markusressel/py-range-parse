import math
import operator
import re
from numbers import Number
from typing import List

RANGE_START_INCLUSIVE = "["
RANGE_START_EXCLUSIVE = "]"
RANGE_END_INCLUSIVE = "]"
RANGE_END_EXCLUSIVE = "["

RANGE_INDICATOR = ".."

FLOAT_INDICATOR = "."


class Range:
    """
    Class to encapsulate a range
    """
    start: Number
    end: Number

    start_inclusive: bool
    end_inclusive: bool

    float: bool = False

    def __init__(self, start: Number, end: Number, start_inclusive: bool = True, end_inclusive: bool = True):
        self.start_inclusive = start_inclusive
        self.end_inclusive = end_inclusive
        if start > end:
            self.start = end
            self.end = start
        else:
            self.start = start
            self.end = end

        if isinstance(start, float) or isinstance(end, float):
            self.float = True

    @property
    def start_comparison_operator(self) -> operator:
        if self.start_inclusive:
            return operator.le
        else:
            return operator.lt

    @property
    def end_comparison_operator(self) -> operator:
        if self.end_inclusive:
            return operator.le
        else:
            return operator.lt

    def __contains__(self, item: int or float):
        if not self.float and isinstance(item, float) and not item.is_integer():
            return False

        if self.float:
            item = float(item)
        else:
            item = int(item)
        in_start = self.start_comparison_operator(self.start, item)
        in_end = self.end_comparison_operator(item, self.end)
        return in_start and in_end


def _parse_value(value: str) -> int or float:
    if "inf" in value or "∞" in value:
        result = math.inf
    elif FLOAT_INDICATOR in value:
        result = float(value)
    else:
        result = int(value)

    if value.startswith("-"):
        result = -result

    return result


def parse_range(text: str) -> List[Range] or Range or None:
    """
    Tries to parse the given text input.

    :param text:
    :return: - List of ranges, if the input can not be represented using a single range
             - Range, if the input can be represented using a single range
             - None, if the input was None or no input was found
    :raises: ValueError if the input could not be parsed
    """
    if text is None:
        return None

    # remove any whitespace
    text = re.sub(r"\s+", "", text, flags=re.UNICODE)
    if len(text) <= 0:
        return None

    if text[0] not in {RANGE_START_INCLUSIVE, RANGE_START_EXCLUSIVE}:
        raise ValueError("Unexpected start character '{}'!: {}".format(text[0], text))

    if text[-1] not in {RANGE_END_INCLUSIVE, RANGE_END_EXCLUSIVE}:
        raise ValueError("Unexpected end character '{}'!: {}".format(text[-1], text))

    # remove first and last char and split by item delimiter
    start_inclusive = text[0] == RANGE_START_INCLUSIVE
    end_inclusive = text[-1] == RANGE_END_INCLUSIVE

    segment = text[1:-1]
    start, end = segment.split(RANGE_INDICATOR)
    start = _parse_value(start)
    end = _parse_value(end)

    return Range(start, end, start_inclusive, end_inclusive)
