# Pascal's Triangle Function

This repository contains a Python function that generates Pascal's Triangle up to the specified number of rows.
## Example Usage

```python
# Import the function from 0-pascal_triangle.py
from pascal_triangle import pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    # Example: Generate and print Pascal's Triangle with 5 rows
    print_triangle(pascal_triangle(5))
