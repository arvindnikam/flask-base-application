from app.db import employees

def call(conditions, offset=None, limit=None, sort_column=None, sort_order=None):
    employees = search_employees()

    return {
        "employees": employees,
        "offset": offset,
        "limit": limit,
        "sort_column": sort_column,
        "sort_order": sort_order,
        "count": len(employees),
        "total": len(employees)
    }

def search_employees():
    return [employee.dict() for employee in employees]
