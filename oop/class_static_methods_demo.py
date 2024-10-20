# Define the Calculator class
class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method for adding two numbers
    @staticmethod
    def add(a, b):
        return a + b

    # Class method for multiplying two numbers
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")  # Access the class attribute
        return a * b
