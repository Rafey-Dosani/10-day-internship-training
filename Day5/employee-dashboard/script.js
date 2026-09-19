const API_URL = "https://jsonplaceholder.typicode.com/users";

let employees = [];
let editingEmployeeId = null;


// DOM elements
const employeeList = document.getElementById("employeeList");
const searchInput = document.getElementById("searchInput");
const departmentFilter = document.getElementById("departmentFilter");
const sortSelect = document.getElementById("sortSelect");

const modal = document.getElementById("employeeModal");
const modalTitle = document.getElementById("modalTitle");

const employeeForm = document.getElementById("employeeForm");
const addEmployeeBtn = document.getElementById("addEmployeeBtn");
const closeModal = document.getElementById("closeModal");


// GET employees
async function fetchEmployees() {
    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Failed to fetch employees");
        }

        employees = await response.json();

        // Add department because JSONPlaceholder doesn't provide one
        employees = employees.map(employee => ({
            ...employee,
            department: getDepartment(employee.id)
        }));

        displayEmployees();

    } catch (error) {
        employeeList.innerHTML = `<p>Error: ${error.message}</p>`;
    }
}


// Assign sample departments
function getDepartment(id) {
    const departments = ["IT", "HR", "Finance", "Marketing"];

    return departments[(id - 1) % departments.length];
}


// Display employees
function displayEmployees() {

    let filteredEmployees = [...employees];

    // Search
    const searchText = searchInput.value.toLowerCase();

    if (searchText) {
        filteredEmployees = filteredEmployees.filter(employee =>
            employee.name.toLowerCase().includes(searchText) ||
            employee.username.toLowerCase().includes(searchText) ||
            employee.email.toLowerCase().includes(searchText)
        );
    }

    // Filter
    const department = departmentFilter.value;

    if (department !== "all") {
        filteredEmployees = filteredEmployees.filter(
            employee => employee.department === department
        );
    }

    // Sort
    if (sortSelect.value === "name") {
        filteredEmployees.sort((a, b) =>
            a.name.localeCompare(b.name)
        );
    }

    if (sortSelect.value === "id") {
        filteredEmployees.sort((a, b) => a.id - b.id);
    }


    if (filteredEmployees.length === 0) {
        employeeList.innerHTML = "<p>No employees found.</p>";
        return;
    }


    employeeList.innerHTML = filteredEmployees.map(employee => `

        <div class="employee-card">

            <h3>${employee.name}</h3>

            <p><strong>ID:</strong> ${employee.id}</p>

            <p><strong>Username:</strong> ${employee.username}</p>

            <p><strong>Email:</strong> ${employee.email}</p>

            <p><strong>Department:</strong> ${employee.department}</p>

            <div class="card-actions">

                <button
                    class="details-btn"
                    onclick="showDetails(${employee.id})">
                    Details
                </button>

                <button
                    class="edit-btn"
                    onclick="editEmployee(${employee.id})">
                    Edit
                </button>

                <button
                    class="delete-btn"
                    onclick="deleteEmployee(${employee.id})">
                    Delete
                </button>

            </div>

        </div>

    `).join("");
}


// Details
function showDetails(id) {

    const employee = employees.find(
        employee => employee.id === id
    );

    if (!employee) {
        return;
    }

    alert(`
Name: ${employee.name}
Username: ${employee.username}
Email: ${employee.email}
Department: ${employee.department}
Phone: ${employee.phone}
Website: ${employee.website}
    `);
}


// Open Add modal
addEmployeeBtn.addEventListener("click", () => {

    editingEmployeeId = null;

    modalTitle.textContent = "Add Employee";

    employeeForm.reset();

    modal.classList.remove("hidden");
});


// Close modal
closeModal.addEventListener("click", () => {
    modal.classList.add("hidden");
});


// Add / Edit employee
employeeForm.addEventListener("submit", async (event) => {

    event.preventDefault();

    const employeeData = {
        name: document.getElementById("employeeName").value,
        username: document.getElementById("employeeUsername").value,
        email: document.getElementById("employeeEmail").value,
        department: document.getElementById("employeeDepartment").value
    };


    try {

        if (editingEmployeeId === null) {

            // POST
            const response = await fetch(API_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(employeeData)
            });

            const newEmployee = await response.json();

            employees.push({
                ...newEmployee,
                id: employees.length + 1
            });

        } else {

            // PUT
            const response = await fetch(
                `${API_URL}/${editingEmployeeId}`,
                {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(employeeData)
                }
            );

            const updatedEmployee = await response.json();

            employees = employees.map(employee =>
                employee.id === editingEmployeeId
                    ? {
                        ...employee,
                        ...updatedEmployee,
                        department: employeeData.department
                    }
                    : employee
            );
        }

        modal.classList.add("hidden");

        displayEmployees();

    } catch (error) {
        alert(`Error: ${error.message}`);
    }
});


// Edit employee
function editEmployee(id) {

    const employee = employees.find(
        employee => employee.id === id
    );

    if (!employee) {
        return;
    }

    editingEmployeeId = id;

    modalTitle.textContent = "Edit Employee";

    document.getElementById("employeeName").value =
        employee.name;

    document.getElementById("employeeUsername").value =
        employee.username;

    document.getElementById("employeeEmail").value =
        employee.email;

    document.getElementById("employeeDepartment").value =
        employee.department;

    modal.classList.remove("hidden");
}


// Delete employee
async function deleteEmployee(id) {

    const confirmed = confirm(
        "Are you sure you want to delete this employee?"
    );

    if (!confirmed) {
        return;
    }

    try {

        // DELETE
        const response = await fetch(
            `${API_URL}/${id}`,
            {
                method: "DELETE"
            }
        );

        if (!response.ok) {
            throw new Error("Failed to delete employee");
        }

        employees = employees.filter(
            employee => employee.id !== id
        );

        displayEmployees();

    } catch (error) {
        alert(`Error: ${error.message}`);
    }
}


// Event listeners
searchInput.addEventListener("input", displayEmployees);

departmentFilter.addEventListener("change", displayEmployees);

sortSelect.addEventListener("change", displayEmployees);


// Start application
fetchEmployees();