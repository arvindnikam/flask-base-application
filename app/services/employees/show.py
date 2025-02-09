from app.db import employees
from app.exceptions import InvalidDataError

def call(employee_id):
    if not (employee := get_employee(employee_id)):
        raise InvalidDataError('Invalid employee id')

    return employee.dict()

def get_employee(employee_id):
    for employee in employees:
        if employee.employee_id == employee_id:
            return employee
