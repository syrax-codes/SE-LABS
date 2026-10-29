
from electricity_bill import energy_charge, late_fee, subsidy


def test_energy_charge_unit_slabs():
    assert energy_charge(0, "domestic") == 50
    assert energy_charge(50, "domestic") == 200
    assert energy_charge(100, "domestic") == 350
    assert energy_charge(200, "domestic") == 850
    assert energy_charge(300, "domestic") == 1350
    assert energy_charge(301, "domestic") == 1358


def test_energy_charge_commercial():
    assert energy_charge(50, "commercial") == 450


def test_energy_charge_invalid_connection():
    try:
        energy_charge(50, "industrial")
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert str(exc) == "unknown connection"


def test_energy_charge_negative_units():
    try:
        energy_charge(-1, "domestic")
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert str(exc) == "invalid units"


def test_late_fee():
    assert late_fee(500, 0) == 0
    assert late_fee(500, -1) == 0
    assert late_fee(500, 10) == 50
    assert late_fee(500, 15) == 50
    assert late_fee(500, 16) == 100
    assert late_fee(2000, 20) == 100
    assert late_fee(2500, 20) == 225


def test_subsidy():
    assert subsidy(80, True, False) == 50
    assert subsidy(80, False, False) == 0
    assert subsidy(150, True, False) == 0
    assert subsidy(150, False, True) == 100
    assert subsidy(80, True, True) == 150
    assert subsidy(350, False, True) == 0
