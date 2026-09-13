from employee import Employee
from employee_service import EmployeeService


def print_menu():

    print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")

    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Search Employee")
    print("5. List All Employees")
    print("6. Filter Employees by Department")
    print("7. Sort Employees by Salary")
    print("8. View Statistics")
    print("9. Exit")


def get_employee_input():

    employee_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    return Employee(
        employee_id,
        name,
        age,
        department,
        salary
    )


def main():

    service = EmployeeService()

    while True:

        print_menu()

        try:

            choice = int(input("\nEnter your choice: "))

            # Add Employee
            if choice == 1:

                employee = get_employee_input()
                service.add_employee(employee)

            # Update Employee
            elif choice == 2:

                employee_id = int(
                    input("Enter Employee ID to update: ")
                )

                name = input("Enter New Name: ")
                age = int(input("Enter New Age: "))
                department = input("Enter New Department: ")
                salary = float(input("Enter New Salary: "))

                service.update_employee(
                    employee_id,
                    name,
                    age,
                    department,
                    salary
                )

            # Delete Employee
            elif choice == 3:

                employee_id = int(
                    input("Enter Employee ID to delete: ")
                )

                service.delete_employee(employee_id)

            # Search Employee
            elif choice == 4:

                employee_id = int(
                    input("Enter Employee ID to search: ")
                )

                employee = service.search_employee(employee_id)

                if employee:
                    print("\nEmployee Found:")
                    print(employee)

                else:
                    print("Employee not found.")

            # List Employees
            elif choice == 5:

                print("\n========== ALL EMPLOYEES ==========")
                service.list_employees()

            # Filter Employees
            elif choice == 6:

                department = input("Enter Department: ")

                employees = service.filter_by_department(
                    department
                )

                if employees:

                    print("\n========== FILTERED EMPLOYEES ==========")

                    for employee in employees:
                        print(employee)

                else:
                    print("No employees found.")

            # Sort Employees
            elif choice == 7:

                employees = service.sort_by_salary()

                print("\n========== EMPLOYEES SORTED BY SALARY ==========")

                for employee in employees:
                    print(employee)

            # Statistics
            elif choice == 8:

                statistics = service.get_statistics()

                if statistics:

                    print("\n========== STATISTICS ==========")

                    print(
                        f"Total Employees: "
                        f"{statistics['total_employees']}"
                    )

                    print(
                        f"Average Salary: "
                        f"{statistics['average_salary']:.2f}"
                    )

                    print(
                        f"Minimum Salary: "
                        f"{statistics['minimum_salary']}"
                    )

                    print(
                        f"Maximum Salary: "
                        f"{statistics['maximum_salary']}"
                    )

                else:
                    print("No employees available.")

            # Exit
            elif choice == 9:

                print("Exiting application...")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as error:
            print(f"Error: {error}")

        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()