# OOP_CVUT
Tasks from course OOP at CVUT
Second task which is creating unique usernames same as in CVUT KOS system

# Create Usernames

This Python project provides a utility function, `create_usernames`, to generate unique usernames for a list of students. The project resolves duplicates and filters only active students, producing a clean and structured output.

## Features

- Generates usernames based on student names.
- Handles duplicate usernames by appending unique counters.
- Filters out inactive students.
- Adheres to Python's best practices (PEP 8).

## How It Works

The function takes a dictionary containing:

- `students`: A list of full names (e.g., `"John Doe"`).
- `active`: A corresponding list of boolean values indicating active status.

### Example Input
```python
{
    "students": ["Adam Levine", "Monica Muller", "John Deere", "John Deere"],
    "active": [True, False, True, True]
}
```

### Example Output
```python
{
    "students": ["Adam Levine", "John Deere", "John Deere"],
    "active": [True, True, True],
    "usernames": ["levinada", "deerejoh", "deerejo2"]
}
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Palo124/OOP_CVUT
   ```
2. Navigate to the project directory:
   ```bash
   cd create_usernames
   ```

## Usage

1. Import the function into your project:
   ```python
   from TaskPP_usernames_Refactor import create_usernames
   ```
2. Use the function with your data:
   ```python
   data = {
       "students": ["Adam Levine", "Monica Muller", "John Deere", "John Deere"],
       "active": [True, False, True, True],
   }
   result = create_usernames(data)
   print(result)
   ```

## Testing

A test case is included in the `__main__` section of the script. Run the script to verify that the function works as expected:
```bash
python create_usernames.py
```


"# OOP_CVUT" 
