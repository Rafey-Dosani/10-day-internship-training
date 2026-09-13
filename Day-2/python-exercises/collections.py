# Lists

numbers = [10, 20, 30, 40]

numbers.append(50)
numbers.remove(20)

print("List:", numbers)


# Tuples

coordinates = (10, 20)

print("Tuple:", coordinates)


# Sets

values = {1, 2, 3, 3, 4, 4}

print("Set:", values)

values.add(5)


# Dictionaries

student = {
    "id": 101,
    "name": "Rafey",
    "branch": "CSE"
}

print("\nDictionary:")
print(student)

print("Name:", student["name"])

student["age"] = 21

for key, value in student.items():
    print(key, ":", value)