from app.db import employees
from app.models.employee import Employee

def call(request):
    employee = Employee(**request)
    employees.append(employee)
    return employee.dict()
