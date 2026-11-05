
import pytest
from hypothesis import given, strategies as st
from electricity_bill import units_consumed, daily_average, tariff_rate


@given(st.text() | st.none())
def test_units_consumed_no_unexpected_crash(value):
    try:
        result = units_consumed(value)
        assert isinstance(result, int)
        assert result >= 0
    except ValueError:
        pass


@given(st.text() | st.none())
def test_daily_average_no_unexpected_crash(value):
    try:
        result = daily_average(value)
        assert isinstance(result, (int, float))
        assert result >= 0
    except ValueError:
        pass


@given(st.text() | st.none())
def test_tariff_rate_no_unexpected_crash(value):
    try:
        result = tariff_rate(value)
        assert isinstance(result, int)
        assert result > 0
    except ValueError:
        pass


def test_valid_inputs():
    assert units_consumed("1200:1350") == 150
    assert daily_average("5,7,6") == 6.0
    assert tariff_rate("DOM-A") == 3
    assert tariff_rate("COM-B") == 12


def test_invalid_inputs_are_rejected():
    with pytest.raises(ValueError):
        units_consumed("1200:")

    with pytest.raises(ValueError):
        daily_average("5,,6")

    with pytest.raises(ValueError):
        tariff_rate("XYZ-A")
