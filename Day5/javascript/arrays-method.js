const employees = [
    { id: 1, name: "Rahul", department: "IT", salary: 50000 },
    { id: 2, name: "Aisha", department: "HR", salary: 45000 },
    { id: 3, name: "John", department: "IT", salary: 60000 },
    { id: 4, name: "Sara", department: "Finance", salary: 55000 }
];

// map()
// Create a new array
const names = employees.map(employee => employee.name);

console.log("Names:", names);

// filter()
// Get employees from IT
const itEmployees = employees.filter(
    employee => employee.department === "IT"
);

console.log("IT Employees:", itEmployees);

// reduce()
// Calculate total salary
const totalSalary = employees.reduce(
    (total, employee) => total + employee.salary,
    0
);

console.log("Total Salary:", totalSalary);

// find()
// Find employee with ID 3
const employee = employees.find(employee => employee.id === 3);

console.log("Employee:", employee);

// some()
// Check if any employee earns more than 55000
const highSalaryEmployee = employees.some(
    employee => employee.salary > 55000
);

console.log("Salary > 55000:", highSalaryEmployee);

// every()
// Check whether all employees earn more than 40000
const allAbove40000 = employees.every(
    employee => employee.salary > 40000
);

console.log("All > 40000:", allAbove40000);

// sort()
// Sort by salary - ascending
const sortedBySalary = [...employees].sort(
    (a, b) => a.salary - b.salary
);

console.log("Sorted by Salary:", sortedBySalary);

// Sort by name
const sortedByName = [...employees].sort(
    (a, b) => a.name.localeCompare(b.name)
);

console.log("Sorted by Name:", sortedByName);