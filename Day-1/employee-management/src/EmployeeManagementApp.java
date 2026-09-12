import java.util.List;
import java.util.Scanner;

public class EmployeeManagementApp {

    private static Scanner scanner = new Scanner(System.in);
    private static EmployeeService employeeService =
            new EmployeeService();

    public static void main(String[] args) {

        int choice;

        do {

            displayMenu();

            System.out.print("Enter your choice: ");
            choice = getIntInput();

            switch (choice) {

                case 1:
                    addEmployee();
                    break;

                case 2:
                    updateEmployee();
                    break;

                case 3:
                    deleteEmployee();
                    break;

                case 4:
                    searchEmployee();
                    break;

                case 5:
                    listAllEmployees();
                    break;

                case 6:
                    findHighestSalaryEmployee();
                    break;

                case 7:
                    calculateAverageSalary();
                    break;

                case 8:
                    filterEmployeesByDepartment();
                    break;

                case 9:
                    System.out.println("Exiting application...");
                    break;

                default:
                    System.out.println("Invalid choice. Please try again.");
            }

        } while (choice != 9);

        scanner.close();
    }

    public static void displayMenu() {

        System.out.println("\n=================================");
        System.out.println(" EMPLOYEE MANAGEMENT SYSTEM");
        System.out.println("=================================");

        System.out.println("1. Add Employee");
        System.out.println("2. Update Employee");
        System.out.println("3. Delete Employee");
        System.out.println("4. Search Employee by ID");
        System.out.println("5. List All Employees");
        System.out.println("6. Find Employee with Highest Salary");
        System.out.println("7. Calculate Average Salary");
        System.out.println("8. Filter Employees by Department");
        System.out.println("9. Exit");

        System.out.println("=================================");
    }

    public static void addEmployee() {

        System.out.print("Enter Employee ID: ");
        int id = getIntInput();

        System.out.print("Enter Employee Name: ");
        String name = scanner.nextLine();

        System.out.print("Enter Department: ");
        String department = scanner.nextLine();

        System.out.print("Enter Salary: ");
        double salary = getDoubleInput();

        Employee employee =
                new Employee(id, name, department, salary);

        boolean added = employeeService.addEmployee(employee);

        if (added) {
            System.out.println("Employee added successfully.");
        } else {
            System.out.println(
                    "Employee with this ID already exists.");
        }
    }

    public static void updateEmployee() {

        System.out.print("Enter Employee ID to update: ");
        int id = getIntInput();

        Employee employee =
                employeeService.searchEmployeeById(id);

        if (employee == null) {
            System.out.println("Employee not found.");
            return;
        }

        System.out.print("Enter New Name: ");
        String name = scanner.nextLine();

        System.out.print("Enter New Department: ");
        String department = scanner.nextLine();

        System.out.print("Enter New Salary: ");
        double salary = getDoubleInput();

        boolean updated =
                employeeService.updateEmployee(
                        id, name, department, salary);

        if (updated) {
            System.out.println(
                    "Employee updated successfully.");
        } else {
            System.out.println("Employee not found.");
        }
    }

    public static void deleteEmployee() {

        System.out.print("Enter Employee ID to delete: ");
        int id = getIntInput();

        boolean deleted =
                employeeService.deleteEmployee(id);

        if (deleted) {
            System.out.println(
                    "Employee deleted successfully.");
        } else {
            System.out.println("Employee not found.");
        }
    }

    public static void searchEmployee() {

        System.out.print("Enter Employee ID: ");
        int id = getIntInput();

        Employee employee =
                employeeService.searchEmployeeById(id);

        if (employee == null) {
            System.out.println("Employee not found.");
        } else {
            System.out.println("\nEmployee Found:");
            System.out.println(employee);
        }
    }

    public static void listAllEmployees() {

        List<Employee> employees =
                employeeService.getAllEmployees();

        if (employees.isEmpty()) {
            System.out.println("Employee list is empty.");
            return;
        }

        System.out.println("\n----- All Employees -----");

        for (Employee employee : employees) {
            System.out.println(employee);
            System.out.println("-------------------------");
        }
    }

    public static void findHighestSalaryEmployee() {

        Employee employee =
                employeeService.getHighestSalaryEmployee();

        if (employee == null) {
            System.out.println("Employee list is empty.");
        } else {
            System.out.println(
                    "\nEmployee with Highest Salary:");

            System.out.println(employee);
        }
    }

    public static void calculateAverageSalary() {

        List<Employee> employees =
                employeeService.getAllEmployees();

        if (employees.isEmpty()) {
            System.out.println("Employee list is empty.");
            return;
        }

        double averageSalary =
                employeeService.getAverageSalary();

        System.out.printf(
                "Average Salary: %.2f%n",
                averageSalary);
    }

    public static void filterEmployeesByDepartment() {

        List<Employee> allEmployees =
                employeeService.getAllEmployees();

        if (allEmployees.isEmpty()) {
            System.out.println("Employee list is empty.");
            return;
        }

        System.out.print("Enter Department: ");
        String department = scanner.nextLine();

        List<Employee> filteredEmployees =
                employeeService
                        .getEmployeesByDepartment(department);

        if (filteredEmployees.isEmpty()) {

            System.out.println(
                    "No employees found in this department.");

        } else {

            System.out.println(
                    "\nEmployees in " + department +
                    " Department:");

            for (Employee employee : filteredEmployees) {

                System.out.println(employee);
                System.out.println("-------------------------");
            }
        }
    }

    public static int getIntInput() {

        while (!scanner.hasNextInt()) {

            System.out.print(
                    "Invalid input. Enter a valid number: ");

            scanner.next();
        }

        int value = scanner.nextInt();
        scanner.nextLine();

        return value;
    }

    public static double getDoubleInput() {

        while (!scanner.hasNextDouble()) {

            System.out.print(
                    "Invalid input. Enter a valid salary: ");

            scanner.next();
        }

        double value = scanner.nextDouble();
        scanner.nextLine();

        return value;
    }
} 