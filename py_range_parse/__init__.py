import math
import operator
import re
from typing import Optional, Union

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
    is_float = False

    def __init__(
        self,
        start: Union[float, int],
        end: Union[float, int],
        start_inclusive: bool = True,
        end_inclusive: bool = True
    ):
        if start > end:
            self.start = end
            self.end = start
            self.start_inclusive = end_inclusive
            self.end_inclusive = start_inclusive
        else:
            self.start = start
            self.end = end
            self.start_inclusive = start_inclusive
            self.end_inclusive = end_inclusive

        self._ensure_typing()

    def _ensure_typing(self):
        if isinstance(self.start, float) or isinstance(self.end, float):
            self.start = float(self.start)
            self.end = float(self.end)
            self.is_float = True

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

    def __contains__(self, item: Union[int, float]) -> bool:
        if not self.is_float and isinstance(item, float) and not item.is_integer():
            return False

        if self.is_float:
            item = float(item)
        else:
            item = int(item)
        in_start = self.start_comparison_operator(self.start, item)
        in_end = self.end_comparison_operator(item, self.end)
        return in_start and in_end

    def __eq__(self, other):
        if not isinstance(other, Range):
            return False

        return (self.start == other.start and
                self.end == other.end and
                self.start_inclusive == other.start_inclusive and
                self.end_inclusive == other.end_inclusive and
                self.is_float == other.is_float)

    def __gt__(self, other):
        if self.is_float:
            other = float(other)
        else:
            other = int(other)

        return self.start > other

    def __lt__(self, other):
        if self.is_float:
            other = float(other)
        else:
            other = int(other)

        return self.end < other

    def __str__(self):
        result = RANGE_START_INCLUSIVE if self.start_inclusive else RANGE_START_EXCLUSIVE
        result += str(self.start)
        result += RANGE_INDICATOR
        result += str(self.end)
        result += RANGE_END_INCLUSIVE if self.start_inclusive else RANGE_END_EXCLUSIVE
        return result


def _parse_value(value: str) -> Union[int, float]:
    if "inf" in value or "∞" in value:
        result = math.inf
        if value.startswith("-"):
            result = -result
    elif FLOAT_INDICATOR in value:
        result = float(value)
    else:
        result = int(value)

    return result


def parse_range(text: str) -> Optional[Range]:
    """
    Tries to parse the given text input.

    :param text:
    :return: - Range, if the input can be represented using a single range
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
