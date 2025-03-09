# Error handling is essential to ensure robust and predictable code.

# Function to calculate the square of a number
def square(x):
    return x * x


# Test the square function with valid and invalid inputs
try:
    print(square(2))  # Valid input
except TypeError:
    print("Error: Input must be a number.")

try:
    print(square("2"))  # Invalid input
except TypeError:
    print("Error: Input must be a number.")


# Custom exception for authentication errors
class AuthenticationError(Exception):
    """Raised when authentication fails."""
    def __init__(self, message="Invalid username or password"):
        super().__init__(message)


# Simple user authentication system
class UserDatabase:
    def __init__(self):
        # Simulated database: username-password pairs
        self.users = {"admin": "1234", "user1": "password"}

    def authenticate(self, username, password):
        """Authenticate a user with username and password."""
        if username not in self.users or self.users[username] != password:
            raise AuthenticationError("Login failed: incorrect credentials")
        return "Login successful!"


# Test the authentication system
db = UserDatabase()

try:
    print(db.authenticate("admin", "admin"))  # Incorrect password
except AuthenticationError as e:
    print(f"Authentication error: {e}")

try:
    print(db.authenticate("user1", "password"))  # Correct credentials
except AuthenticationError as e:
    print(f"Authentication error: {e}")
