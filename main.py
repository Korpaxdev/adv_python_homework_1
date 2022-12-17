from datetime import datetime

from application.db.people import get_employees
from application.salary import calculate_salary
from application.parser import get_netology_h1

if __name__ == '__main__':
    print('today date is', datetime.now().date())
    calculate_salary()
    get_employees()
    # title = get_netology_h1(30)
    # if title:
    #     print('Привет', title)
