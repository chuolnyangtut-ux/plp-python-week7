# Assignment: Shopping List Manager

## File Descriptions
* **list_warmup.py**: Demonstrates basic list creation, index access, appending, removing, and length checking.
* **shopping_list.py**: An interactive command-line shopping list manager supporting add, remove, show, and exit features with safety checks.
* **list_report.py**: Generates a numbered report, counts items with names longer than four characters, and finds the longest item name.

## Discussion
**Why is it safer to check `in` before calling `.remove()`?**
Checking if an item exists in the list using the `in` keyword before calling `.remove()` prevents the program from crashing. If you try to remove an item that is not present in the list using `.remove()` directly, Python raises a `ValueError`. Using `in` allows the program to handle missing items gracefully by displaying a warning message instead.
# plp-python-week7