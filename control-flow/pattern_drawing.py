# pattern_drawing.py

# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Draw the Pattern using a while loop
while row < size:
    # Use a for loop to print asterisks side by side
    for col in range(size):
        print("*", end="")
    
    # Print a newline character to move to the next row
    print()
    
    # Increment the row counter
    row += 1
