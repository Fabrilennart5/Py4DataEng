# Log management is essential for identifying and resolving issues in real-time.
# It helps analyze patterns and trends to improve system security and stability.

import logging

# Logging levels (from least to most critical):
# DEBUG (10), INFO (20), WARNING (30), ERROR (40), CRITICAL (50)

# Configure logging to write to a file with a specific format
logging.basicConfig(
    filename="data_processing.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",  # Format: timestamp, level, message
)


def process_numbers(numbers):
    """
    Process a list of numbers: calculate sum and average.
    Logs key steps and errors for debugging and monitoring.
    """
    logging.info("Starting number processing...")

    if not numbers:
        logging.warning("The list is empty. No processing will be done.")
        return None

    try:
        total = sum(numbers)
        average = total / len(numbers)

        logging.debug(f"Total: {total}, Count: {len(numbers)}, Average: {average}")
        logging.info("Processing completed successfully.")

        return total, average

    except Exception as e:
        logging.error(f"An error occurred during processing: {e}")
        return None


# Example usage
numbers = [10, 20, 30, 40, 50]
process_numbers(numbers)

# Simulating an error with invalid data
invalid_data = [10, "twenty", 30]  # This will cause an error
process_numbers(invalid_data)
