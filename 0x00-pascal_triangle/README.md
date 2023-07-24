# Pascal's Triangle Function

This repository contains a Python function that generates Pascal's Triangle up to the specified number of rows.

## Function Details

### `def pascal_triangle(n):`

This function takes an integer `n` as input and returns a list of lists of integers representing Pascal's Triangle up to the `n`th row.

#### Parameters:

- `n` (int): The number of rows to generate for Pascal's Triangle.

#### Returns:

- `list`: A list of lists of integers representing Pascal's Triangle.

#### Constraints:

- Returns an empty list if `n <= 0`.
- Assumes `n` will always be an integer.

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
