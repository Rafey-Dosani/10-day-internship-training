const API_URL = "https://jsonplaceholder.typicode.com/users";

// GET
async function getEmployees() {
    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Failed to fetch employees");
        }

        const employees = await response.json();

        console.log("Employees:", employees);
    } catch (error) {
        console.error("GET Error:", error.message);
    }
}


// POST
async function addEmployee() {
    const employee = {
        name: "Rafey",
        username: "rafey",
        email: "rafey@example.com"
    };

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(employee)
        });

        const data = await response.json();

        console.log("Added Employee:", data);
    } catch (error) {
        console.error("POST Error:", error.message);
    }
}


// PUT
async function updateEmployee(id) {
    const updatedEmployee = {
        name: "Rafey Updated",
        username: "rafey",
        email: "updated@example.com"
    };

    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(updatedEmployee)
        });

        const data = await response.json();

        console.log("Updated Employee:", data);
    } catch (error) {
        console.error("PUT Error:", error.message);
    }
}


// DELETE
async function deleteEmployee(id) {
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) {
            throw new Error("Failed to delete employee");
        }

        console.log("Employee deleted successfully");
    } catch (error) {
        console.error("DELETE Error:", error.message);
    }
}


// Test API operations
getEmployees();
// addEmployee();
// updateEmployee(1);
// deleteEmployee(1);