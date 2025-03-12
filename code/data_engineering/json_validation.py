import json
from datetime import datetime

# Path to the JSON file
path = r"D:\Proyectos de codigo\python\code\data_sources\Json_data\transacciones.json"

# Load the JSON file
with open(path, "r", encoding="utf-8") as file:
    data = json.load(file)


# 1. Check if a key exists in a dictionary
def validate_key_exists(dictionary, key):
    """I check if the given key exists in the dictionary."""
    if key not in dictionary:
        print(f"Error: Missing required key '{key}'")
        return False
    return True


# 2. Validate that a value is a non-negative number
def validate_positive_number(value):
    """I ensure the value is a non-negative number."""
    if not isinstance(value, (int, float)) or value < 0:
        print(f"Error: '{value}' must be a non-negative number")
        return False
    return True


# 3. Validate that a value is a non-empty string
def validate_non_empty_string(value):
    """I check if the value is a non-empty string."""
    if not isinstance(value, str) or not value.strip():
        print(f"Error: '{value}' must be a non-empty string")
        return False
    return True


# 4. Validate that a value is a positive integer
def validate_positive_integer(value):
    """I ensure the value is a positive integer."""
    if not isinstance(value, int) or value <= 0:
        print(f"Error: '{value}' must be a positive integer")
        return False
    return True


# 5. Validate that a value is a valid email address
def validate_email(email):
    """I check if the value follows a valid email format."""
    if "@" not in email or "." not in email.split("@")[1]:
        print(f"Error: '{email}' must be a valid email address")
        return False
    return True


# 6. Validate that a list has an exact number of elements
def validate_list_length(lst, expected_length):
    """I ensure the list has exactly the expected number of elements."""
    if not isinstance(lst, list) or len(lst) != expected_length:
        print(f"Error: List must have exactly {expected_length} elements")
        return False
    return True


# 7. Validate that a date is in YYYY-MM-DD format
def validate_date(date_str):
    """I check if the date string is correctly formatted as YYYY-MM-DD."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        print(f"Error: '{date_str}' must be in YYYY-MM-DD format")
        return False


# Running validations with the loaded JSON data
print("Validating key 'name':", validate_key_exists(data, "name"))
print(
    "Validating key 'address':", validate_key_exists(data, "address")
)  # Expected to fail

print(
    "\nValidating that 'age' is a non-negative number:",
    validate_positive_number(data.get("age", -1)),
)
print(
    "Validating that 'age' is a positive integer:",
    validate_positive_integer(data.get("age", -1)),
)

print(
    "\nValidating that 'name' is a non-empty string:",
    validate_non_empty_string(data.get("name", "")),
)
print(
    "Validating that 'email' is a valid email:", validate_email(data.get("email", ""))
)

print(
    "\nValidating that 'scores' has 3 elements:",
    validate_list_length(data.get("scores", []), 3),
)
print(
    "Validating that 'birthdate' is in YYYY-MM-DD format:",
    validate_date(data.get("birthdate", "")),
)
