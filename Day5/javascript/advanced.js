// Scope
let globalMessage = "Global";

function scopeExample() {
    let localMessage = "Local";

    console.log(globalMessage);
    console.log(localMessage);
}

scopeExample();


// Hoisting
console.log(hoistedFunction());

function hoistedFunction() {
    return "Function is hoisted";
}


// Closure
function createCounter() {
    let count = 0;

    return function () {
        count++;
        return count;
    };
}

const counter = createCounter();

console.log("Counter:", counter());
console.log("Counter:", counter());
console.log("Counter:", counter());


// Callback
function processEmployee(employee, callback) {
    console.log(`Processing ${employee.name}`);
    callback();
}

processEmployee(
    { name: "Rafey" },
    () => console.log("Employee processed")
);


// Promise
const employeePromise = new Promise((resolve, reject) => {
    const success = true;

    if (success) {
        resolve("Employee data loaded");
    } else {
        reject("Failed to load employee data");
    }
});

employeePromise
    .then(message => console.log(message))
    .catch(error => console.error(error));


// async / await
async function loadEmployee() {
    try {
        const result = await employeePromise;
        console.log("Async:", result);
    } catch (error) {
        console.error("Error:", error);
    }
}

loadEmployee();


// Error handling
function divide(a, b) {
    if (b === 0) {
        throw new Error("Cannot divide by zero");
    }

    return a / b;
}

try {
    console.log(divide(10, 2));
    console.log(divide(10, 0));
} catch (error) {
    console.error("Error:", error.message);
}


// Event loop
console.log("Start");

setTimeout(() => {
    console.log("setTimeout");
}, 0);

Promise.resolve().then(() => {
    console.log("Promise");
});

console.log("End");