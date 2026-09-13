from employee import Employee
from file_handler import FileHandler


class EmployeeService:

    def __init__(self):
        self.file_handler = FileHandler()

        # Load employee data from JSON
        data = self.file_handler.load_data()

        # Convert dictionaries into Employee objects
        self.employees = [
            Employee.from_dict(employee)
            for employee in data
        ]

    # Save employees to JSON file
    def save_employees(self):
        data = [
            employee.to_dict()
            for employee in self.employees
        ]

        self.file_handler.save_data(data)

    # Add employee
    def add_employee(self, employee):

        for existing_employee in self.employees:

            if existing_employee.employee_id == employee.employee_id:
                raise ValueError("Employee ID already exists.")

        self.employees.append(employee)

        self.save_employees()

        print("Employee added successfully.")

    # List all employees
    def list_employees(self):

        if not self.employees:
            print("No employees found.")
            return

        for employee in self.employees:
            print(employee)

    # Search employee by ID
    def search_employee(self, employee_id):

        for employee in self.employees:

            if employee.employee_id == employee_id:
                return employee

        return None

    # Update employee
    def update_employee(
            self,
            employee_id,
            name,
            age,
            department,
            salary):

        employee = self.search_employee(employee_id)

        if employee is None:
            raise ValueError("Employee not found.")

        employee.name = name
        employee.age = age
        employee.department = department
        employee.salary = salary

        self.save_employees()

        print("Employee updated successfully.")

    # Delete employee
    def delete_employee(self, employee_id):

        employee = self.search_employee(employee_id)

        if employee is None:
            raise ValueError("Employee not found.")

        self.employees.remove(employee)

        self.save_employees()

        print("Employee deleted successfully.")

    # Filter employees by department
    def filter_by_department(self, department):

        filtered_employees = [
            employee
            for employee in self.employees
            if employee.department.lower() == department.lower()
        ]

        return filtered_employees

    # Sort employees by salary (ascending)
    def sort_by_salary(self):

        return sorted(
            self.employees,
            key=lambda employee: employee.salary
        )

    # Sort employees by salary (descending)
    def sort_by_salary_descending(self):

        return sorted(
            self.employees,
            key=lambda employee: employee.salary,
            reverse=True
        )

    # Get employee statistics
    def get_statistics(self):

        if not self.employees:
            return None

        salaries = [
            employee.salary
            for employee in self.employees
        ]

        average_salary = sum(salaries) / len(salaries)

        return {
            "total_employees": len(self.employees),
            "average_salary": average_salary,
            "minimum_salary": min(salaries),
            "maximum_salary": max(salaries)
        }