import java.util.ArrayList;
import java.util.List;

public class EmployeeService {

    private List<Employee> employees;

    public EmployeeService() {
        employees = new ArrayList<>();
    }

    public boolean addEmployee(Employee employee) {

        if (searchEmployeeById(employee.getId()) != null) {
            return false;
        }

        employees.add(employee);
        return true;
    }

    public boolean updateEmployee(int id, String name,
                                  String department, double salary) {

        Employee employee = searchEmployeeById(id);

        if (employee == null) {
            return false;
        }

        employee.setName(name);
        employee.setDepartment(department);
        employee.setSalary(salary);

        return true;
    }

    public boolean deleteEmployee(int id) {

        Employee employee = searchEmployeeById(id);

        if (employee == null) {
            return false;
        }

        employees.remove(employee);
        return true;
    }

    public Employee searchEmployeeById(int id) {

        for (Employee employee : employees) {

            if (employee.getId() == id) {
                return employee;
            }
        }

        return null;
    }

    public List<Employee> getAllEmployees() {
        return employees;
    }

    public Employee getHighestSalaryEmployee() {

        if (employees.isEmpty()) {
            return null;
        }

        Employee highestSalaryEmployee = employees.get(0);

        for (Employee employee : employees) {

            if (employee.getSalary() >
                    highestSalaryEmployee.getSalary()) {

                highestSalaryEmployee = employee;
            }
        }

        return highestSalaryEmployee;
    }

    public double getAverageSalary() {

        if (employees.isEmpty()) {
            return 0;
        }

        double totalSalary = 0;

        for (Employee employee : employees) {
            totalSalary += employee.getSalary();
        }

        return totalSalary / employees.size();
    }

    public List<Employee> getEmployeesByDepartment(String department) {

        List<Employee> filteredEmployees = new ArrayList<>();

        for (Employee employee : employees) {

            if (employee.getDepartment()
                    .equalsIgnoreCase(department)) {

                filteredEmployees.add(employee);
            }
        }

        return filteredEmployees;
    }
}