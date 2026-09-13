class Employee:
    def __init__(self, employee_id, name, age, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "salary": self.salary
        }

    @staticmethod
    def from_dict(data):
        return Employee(
            data["employee_id"],
            data["name"],
            data["age"],
            data["department"],
            data["salary"]
        )

    def __str__(self):
        return (
            f"ID: {self.employee_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Department: {self.department} | "
            f"Salary: {self.salary}"
        )