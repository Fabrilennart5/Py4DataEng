# Working with dates and times is essential in data engineering.
# Python's `datetime` module provides tools to handle dates, times, and time intervals.

from datetime import datetime, timedelta

# Get the current date and time
current_datetime = datetime.now()
print("Current datetime:", current_datetime)


def subtract_hours(date, hours):
    """
    Subtract hours from a given datetime.

    Args:
        date (datetime): The datetime object.
        hours (int): Number of hours to subtract.

    Returns:
        datetime: The updated datetime.
    """
    return date - timedelta(hours=hours)


# Example: Subtract 2 hours from the current datetime
print("Datetime after subtracting 2 hours:", subtract_hours(current_datetime, 2))


def format_date(date):
    """
    Format a datetime object into a readable string.

    Args:
        date (datetime): The datetime object.

    Returns:
        str: Formatted date string (YYYY/MM/DD HH:MM:SS).
    """
    return date.strftime("%Y/%m/%d %H:%M:%S")


# Example: Format the datetime after subtracting 2 hours
formatted_date = format_date(subtract_hours(current_datetime, 2))
print("Formatted datetime:", formatted_date)


# Additional examples of using the datetime module

# 1. Create a specific datetime
specific_date = datetime(2023, 10, 31, 15, 30)  # October 31, 2023, 3:30 PM
print("Specific datetime:", specific_date)

# 2. Add days to a datetime
future_date = specific_date + timedelta(days=10)
print("Datetime after adding 10 days:", future_date)

# 3. Compare two datetimes
if future_date > current_datetime:
    print("Future date is after the current datetime.")

# 4. Extract components from a datetime
print("Year:", specific_date.year)
print("Month:", specific_date.month)
print("Day:", specific_date.day)
print("Hour:", specific_date.hour)
print("Minute:", specific_date.minute)

# 5. Calculate the difference between two datetimes
time_difference = future_date - specific_date
print("Time difference between future_date and specific_date:", time_difference)
