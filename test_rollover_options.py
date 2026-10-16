import pytest

from millify import millify


@pytest.mark.parametrize(
    "value,expected", [(999999, "1.00M-count"), (-999999, "-1.00M-count")]
)
def test_rollover_keeps_custom_suffix_and_fixed_precision(value, expected):
    prefixes = ["k-count", "M-count"]

    assert millify(value, precision=2, drop_nulls=False, prefixes=prefixes) == expected
    assert prefixes == ["k-count", "M-count"]


def test_rollover_stops_at_last_custom_suffix():
    assert (
        millify(999999, precision=2, drop_nulls=False, prefixes=["k-count"])
        == "1000.00k-count"
    )
