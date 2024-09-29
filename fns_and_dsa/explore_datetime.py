from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted current date and time
    print(f"Current date and time: {formatted_date}")
    return current_date

# Part 2: Calculate a future date based on the user's input
def calculate_future_date(current_date):
    # Prompt the user to enter a number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date by adding the days to the current date
    future_date = current_date + timedelta(days=days_to_add)
    # Print the future date in "YYYY-MM-DD" format
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Main function to run the script
def main():
    # Part 1: Display the current date and time
    current_date = display_current_datetime()
    # Part 2: Calculate and display the future date
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
