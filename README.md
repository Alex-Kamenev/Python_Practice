# Python practice

Small Python exercises. `HasDuplicates.py` detects equal values in an iterable of hashable items using a set, including values whose hashes collide.

Requires Python 3; no third-party packages.

```text
python HasDuplicates.py
python -m unittest discover -p "test_*.py"
```

Importing the function does not run the random demonstration. Unhashable items such as lists raise `TypeError`.
