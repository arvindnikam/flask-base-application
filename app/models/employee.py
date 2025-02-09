from dataclasses import dataclass, asdict

@dataclass
class Employee:
    employee_id: int
    name: str
    department: str
    salary: int

    def dict(self):
        return asdict(self)
