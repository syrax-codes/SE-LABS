# Lab 5: Static Code Analysis - Issue Table

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument | Bug / Code Quality | 8 | `history=[]` can share a mutable list across function calls. | Changed the default to `None` and initialized a new list inside the function. |
| Hardcoded password | Security | 5 | A password was stored directly in the source code. | Removed the unused hardcoded password. |
| SQL string construction | Security | 9 | User-controlled values were interpolated into an SQL statement. | Used parameterized SQL queries. |
| Unsafe `eval()` | Security | 21 | `eval()` can execute arbitrary Python expressions. | Replaced it with a restricted arithmetic-expression evaluator. |
| Broad exception handling | Code Quality | 22 | Catching `Exception` can hide unexpected errors. | Caught specific exceptions relevant to the calculation. |
| Inconsistent return values | Code Quality | 12–16 | `collect()` returned an amount for a match but implicitly returned `None` otherwise. | Explicitly returned `None` when no matching due exists. |
| Naming convention | Code Style | 8 | `addDue()` did not follow Python's `snake_case` naming convention. | Renamed it to `add_due()`. |
| Missing docstrings | Code Quality | Multiple | The module and functions lacked documentation. | Added descriptive docstrings. |
| Unnecessary `None` comparison | Code Style | 29 | `rows != None` was unnecessary because `fetchall()` returns a list. | Returned the list comprehension directly. |
| Formatting violations | Code Style | Multiple | Flake8 identified long lines and incorrect blank-line formatting. | Reformatted the source to satisfy Flake8. |

## Verification

- Pylint before fixes: 5.81/10
- Pylint after fixes: 10.00/10
- Bandit before fixes: 3 findings (1 low, 2 medium)
- Bandit after fixes: No issues identified
- Flake8 before fixes: 5 violations
- Flake8 after fixes: No violations