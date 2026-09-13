import json


class FileHandler:

    def __init__(self, filename="employees.json"):
        self.filename = filename

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return data

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("Error: Invalid JSON data.")
            return []

        except Exception as error:
            print(f"Error while loading data: {error}")
            return []

    def save_data(self, data):
        try:
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)

        except Exception as error:
            print(f"Error while saving data: {error}")