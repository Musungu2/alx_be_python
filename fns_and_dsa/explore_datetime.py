import datetime

def  display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date():
    days= int(input("Enter number of days: "))
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))
