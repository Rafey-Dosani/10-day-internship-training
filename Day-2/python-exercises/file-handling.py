import json


filename = "sample.json"


data = {
    "name": "Rafey",
    "age": 21,
    "branch": "CSE"
}


# Write data to JSON file

try:

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print("Data written successfully.")


except Exception as error:

    print("Error while writing:", error)


# Read data from JSON file

try:

    with open(filename, "r") as file:
        loaded_data = json.load(file)

    print("\nData read from file:")
    print(loaded_data)


except FileNotFoundError:

    print("File not found.")


except json.JSONDecodeError:

    print("Invalid JSON data.")


except Exception as error:

    print("Unexpected error:", error)