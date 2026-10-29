# Lab 6: Code and Branch Coverage

## Objective
Measure and improve code and branch coverage for the electricity bill application using `pytest` and `coverage.py`.

## Files
- `electricity_bill.py` — Application under test.
- `CodeCoverageTest_PES1UG24CS016_application.py` — Code coverage tests.
- `BranchCoverageTest_PES1UG24CS016_application.py` — Branch coverage tests.
- `code_coverage_screenshot.png` — Code coverage results.
- `branch_coverage_screenshot.png` — Branch coverage results.

## Results
- **Code coverage:** 100% (6 tests passed).
- **Branch coverage:** 100% (4 tests passed; 22 branches, 0 partial branches).

## Run the Tests
Run from the `Lab 6` directory.

**Code coverage**
```powershell
python -m coverage erase
python -m coverage run --source=electricity_bill -m pytest CodeCoverageTest_PES1UG24CS016_application.py
python -m coverage report -m
```

**Branch coverage**
```powershell
python -m coverage erase
python -m coverage run --branch --source=electricity_bill -m pytest BranchCoverageTest_PES1UG24CS016_application.py
python -m coverage report -m
```
