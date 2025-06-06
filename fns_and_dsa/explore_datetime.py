from datetime import *


def display_current_datetime():
    current_date = datetime.now()
    formateDate = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formateDate}")


def calculate_future_date():
    current_date = datetime.now()
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d %H-%M-%S')}")


def main():
    display_current_datetime()
    calculate_future_date()

if __name__ =='__main__':
    main()