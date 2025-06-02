while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a high priority task. Try to complete it soon.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that needs attention today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Schedule it accordingly.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task, but it's time-sensitive. Don’t forget it!")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority entered. Please enter high, medium, or low.")
    
    # Ask if the user wants to enter another task
    another = input("Would you like to enter another task? (yes/no): ").lower()
    if another != "yes":
        print("Good job staying organized. Goodbye!")
        break

