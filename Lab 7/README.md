# Lab 7: Fuzz Testing

## Objective
Use Hypothesis and pytest to identify input-handling bugs in the electricity bill application, fix them, and verify the results.

## Files
- `electricity_bill.py` — Application with input validation.
- `test_electricity_bill.py` — Hypothesis-based fuzz tests and validation tests.
- `Lab7_FuzzTesting_Report.pdf` — Screenshots documenting the testing and fixing process.

## Bugs Identified
Hypothesis exposed invalid-input failures involving:
- Malformed meter readings.
- Empty or invalid daily-unit CSV input.
- Invalid tariff codes and missing values.

The application was updated to validate inputs and raise controlled `ValueError` exceptions.

## Test Results
**Final result: 5 tests passed.**

## Run the Tests
Install dependencies:
```powershell
python -m pip install hypothesis pytest
```

Run:
```powershell
python -m pytest test_electricity_bill.py -v
```

## Sample Application Run
```powershell
python electricity_bill.py
```