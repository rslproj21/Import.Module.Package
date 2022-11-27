from salary import calculate_salary
from people import get_employees
from datetime import datetime

if __name__ == "__main__":
    if calculate_salary and get_employees:
        print(datetime.now(), calculate_salary and get_employees)

