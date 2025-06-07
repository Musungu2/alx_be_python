from datetime import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date

def calculate_future_date():
    days = int(input("Enter number of days: "))
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    print("Current Date and Time:", display_current_datetime())
    print("Future Date:", calculate_future_date())
