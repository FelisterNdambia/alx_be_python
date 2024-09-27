# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder_message = ""

# Process the Task Based on Priority
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task"
    case _:
        reminder_message = "Priority not recognized."

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += ". Consider completing it when you have free time."

# Provide a Customized Reminder
print(f"Reminder: {reminder_message}")

