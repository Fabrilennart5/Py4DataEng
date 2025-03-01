# Log management is key to identifying and resolving real-time issues.
# It enables pattern analysis and trend spotting for
# improved system security and stability.

import logging

# there are for levels of logging
# DEBUG, INFO, WARNING, ERROR, CRITICAL
# these levels are ordered from least to most important
# and  they have a number associated with them
# DEBUG = 10
# INFO = 20
# WARNING = 30
# ERROR = 40
# CRITICAL = 50

# for  configuring the logs we use this:

logging.basicConfig(
    filename="data_processing.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",  # time level message
)


# Function to process a list of numbers
def process_numbers(numbers):
    """
    Process a list of numbers: calculate sum and average.
    Logs important events such as errors and key steps.
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

# Simulating an error with an invalid list
invalid_data = [10, "twenty", 30]  # This will cause an error
process_numbers(invalid_data)
