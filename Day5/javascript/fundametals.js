// let and const
let employeeName = "Rafey";
const employeeId = 101;

// Data types
let age = 21;
let salary = 50000;
let isActive = true;
let department = null;
let address;

console.log(employeeName, age, salary, isActive, department, address);

// Function
function calculateSalary(basic, bonus) {
    return basic + bonus;
}

console.log(calculateSalary(40000, 5000));

// Arrow function
const greetEmployee = (name) => {
    return `Welcome, ${name}`;
};

console.log(greetEmployee(employeeName));

// Array
const skills = ["Java", "SQL", "JavaScript"];

console.log(skills);

// Object
const employee = {
    id: 101,
    name: "Rafey",
    department: "IT",
    salary: 50000
};

console.log(employee);

const { id, name, department: employeeDepartment } = employee;

console.log(id, name, employeeDepartment);
// Array destructuring
const [firstSkill, secondSkill] = skills;

console.log(firstSkill, secondSkill);

// Spread operator
const updatedEmployee = {
    ...employee,
    salary: 55000
};

console.log(updatedEmployee);

// Rest operator
function calculateTotal(...numbers) {
    return numbers.reduce((total, number) => total + number, 0);
}

console.log(calculateTotal(100, 200, 300));

// Template literals
console.log(
    `Employee ${employee.name} works in ${employee.department} department.`
);