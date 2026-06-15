"""Tests for millify()."""
import pytest

from millify import millify


@pytest.mark.parametrize(
    "n, kwargs, expected",
    [
        (0, {}, "0"),
        (999, {}, "999"),
        (1000, {}, "1k"),
        (1000000, {}, "1M"),
        (1234567, {"precision": 2}, "1.23M"),
        (-1500, {"precision": 1}, "-1.5k"),
        # Rounding must carry into the next unit instead of producing
        # an out-of-range mantissa like "1000k".
        (999999, {}, "1M"),
        (999500, {}, "1M"),
        (999999, {"precision": 2}, "1M"),
        (-999999, {}, "-1M"),
        (999999999, {}, "1B"),
    ],
)
def test_millify(n, kwargs, expected):
    assert millify(n, **kwargs) == expected


def test_millify_no_overflow_at_largest_unit():
    # No larger suffix than "Y" exists, so the mantissa is left as-is
    # rather than carrying past the table.
    assert millify(10 ** 27, precision=0).endswith("Y")
