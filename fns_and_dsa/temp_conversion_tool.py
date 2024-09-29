# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion functions

def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using the global factor
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using the global factor
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# User interaction

def main():
    try:
        # Prompt the user to enter a temperature
        temp_input = float(input("Enter the temperature to convert: "))
        
        # Ask the user whether the temperature is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temp_input)
            print(f"{temp_input}°F is {converted_temp}°C")
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temp_input)
            print(f"{temp_input}°C is {converted_temp}°F")
        else:
            # Handle invalid input for unit
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        # Handle invalid temperature input or other errors
        print(f"Error: {e}")
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
