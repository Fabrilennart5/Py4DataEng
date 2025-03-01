# working and having no errors is like dreaming
# so we need to manage the errors


# Define a function to calculate the square of a number
def square(x):
    # Return the square of the input number
    return x * x


# Attempt to execute the square function with a valid input
try:
    # Print the result of squaring the number 2
    print(square(2))
# Catch TypeError exceptions
except TypeError:
    # Print an error message if a TypeError occurs
    print("You have to pass a number")

# Attempt to execute the square function with an invalid input
try:
    # Print the result of squaring the string "2"
    print(square("2"))
# Catch TypeError exceptions
except TypeError:
    # Print an error message if a TypeError occurs
    print("You have to pass a number")


# Also we can create a class to manage the errors
# Python has built-in exceptions like ValueError, TypeError, etc.,
# but sometimes we want to handle more specific situations.
# For example: In an authentication system, a password failure
# shouldn't be a generic ValueError. In a banking system, an
# attempt to withdraw with insufficient funds isn't just a TypeError.


# Custom exception for authentication errors
class AuthenticationError(Exception):
    """
    Custom exception for handling authentication failures.
    """

    def __init__(self, message="Invalid username or password"):
        """
        Initialize the exception with a default authentication failure message.
        """
        self.message = message
        super().__init__(self.message)


class UserDatabase:
    """
    A simple user authentication system.
    """

    def __init__(self):
        # Simulated database: dictionary with username-password pairs
        self.users = {"admin": "1234", "user1": "password"}

    def authenticate(self, username, password):
        """
        Check if the provided username and password match the stored credentials.
        """
        if username not in self.users or self.users[username] != password:
            # Raise a custom exception when authentication fails
            raise AuthenticationError("Login failed: incorrect username or password")
        return "Login successful!"


# Testing the authentication system
db = UserDatabase()

try:
    print(db.authenticate("admin", "admin"))  # Incorrect password
except AuthenticationError as e:
    print(f"Authentication error: {e}")

try:
    print(db.authenticate("user1", "password"))  # Correct credentials
except AuthenticationError as e:
    print(f"Authentication error: {e}")
