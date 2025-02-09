from app.db import employees
from app.models.employee import Employee
from app.exceptions import InvalidDataError

def call(employee_id, request):
    i, employee = get_employee(employee_id)
    if not employee:
        raise InvalidDataError('Invalid employee id')

    employee = Employee(**employee.dict()|request)
    employees[i] = employee
    return employee.dict()

def get_employee(employee_id):
    for i, employee in enumerate(employees):
        if employee.employee_id == employee_id:
            return i, employee

    return None, None
