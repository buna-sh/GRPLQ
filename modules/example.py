# example_module.py

# variables
MODULE_NAME = "Example Module"
VERSION = "1.0.0"

print(f"{MODULE_NAME}: Version {VERSION}")


# Sample function
def greet(name):
    """Greets the given name."""
    return f"Hello, {name}! Welcome to {MODULE_NAME}."

# Sample class
class Calculator:
    """A simple calculator class."""

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Returns the difference of two numbers."""
        return a - b

# Example code for demonstration when the module is loaded directly
if __name__ == "__main__":
    print("This is an example module.")
    print(greet("User"))
    calc = Calculator()
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"5 - 2 = {calc.subtract(5, 2)}")

