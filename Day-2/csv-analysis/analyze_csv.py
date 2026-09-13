import csv
from collections import Counter


FILE_NAME = "data.csv"


def load_data():

    try:

        with open(FILE_NAME, "r", newline="") as file:

            reader = csv.DictReader(file)

            return list(reader)

    except FileNotFoundError:

        print("Error: CSV file not found.")
        return []

    except Exception as error:

        print(f"Error while reading file: {error}")
        return []


def count_records(data):

    return len(data)


def find_missing_values(data):

    missing_values = {}

    if not data:
        return missing_values

    columns = data[0].keys()

    for column in columns:

        count = 0

        for row in data:

            if row[column] is None or row[column].strip() == "":
                count += 1

        missing_values[column] = count

    return missing_values


def find_duplicates(data):

    duplicates = []

    seen = set()

    for row in data:

        row_tuple = tuple(row.values())

        if row_tuple in seen:

            duplicates.append(row)

        else:

            seen.add(row_tuple)

    return duplicates


def get_numeric_values(data, column):

    values = []

    for row in data:

        try:

            value = row[column].strip()

            if value != "":
                values.append(float(value))

        except (ValueError, KeyError):

            continue

    return values


def calculate_statistics(values):

    if not values:
        return None

    return {
        "average": sum(values) / len(values),
        "minimum": min(values),
        "maximum": max(values)
    }


def category_wise_statistics(data):

    categories = {}

    for row in data:

        department = row["department"].strip()

        if department == "":
            department = "Unknown"

        if department not in categories:

            categories[department] = []

        try:

            salary = row["salary"].strip()

            if salary != "":
                categories[department].append(float(salary))

        except ValueError:

            continue

    results = {}

    for department, salaries in categories.items():

        results[department] = {
            "record_count": sum(
                1
                for row in data
                if row["department"].strip() == department
            )
        }

        if salaries:

            results[department]["average_salary"] = (
                sum(salaries) / len(salaries)
            )

            results[department]["minimum_salary"] = min(salaries)

            results[department]["maximum_salary"] = max(salaries)

        else:

            results[department]["average_salary"] = None
            results[department]["minimum_salary"] = None
            results[department]["maximum_salary"] = None

    return results


def print_analysis(data):

    print("\n========== CSV DATA ANALYSIS ==========")

    # Record Count

    print(f"\nTotal Records: {count_records(data)}")

    # Missing Values

    missing_values = find_missing_values(data)

    print("\n---------- Missing Values ----------")

    for column, count in missing_values.items():

        print(f"{column}: {count}")

    # Duplicate Records

    duplicates = find_duplicates(data)

    print("\n---------- Duplicate Records ----------")

    print(f"Total Duplicates: {len(duplicates)}")

    # Salary Statistics

    salaries = get_numeric_values(data, "salary")

    salary_statistics = calculate_statistics(salaries)

    print("\n---------- Salary Statistics ----------")

    if salary_statistics:

        print(
            f"Average Salary: "
            f"{salary_statistics['average']:.2f}"
        )

        print(
            f"Minimum Salary: "
            f"{salary_statistics['minimum']:.2f}"
        )

        print(
            f"Maximum Salary: "
            f"{salary_statistics['maximum']:.2f}"
        )

    else:

        print("No valid salary data available.")

    # Age Statistics

    ages = get_numeric_values(data, "age")

    age_statistics = calculate_statistics(ages)

    print("\n---------- Age Statistics ----------")

    if age_statistics:

        print(
            f"Average Age: "
            f"{age_statistics['average']:.2f}"
        )

        print(
            f"Minimum Age: "
            f"{age_statistics['minimum']:.2f}"
        )

        print(
            f"Maximum Age: "
            f"{age_statistics['maximum']:.2f}"
        )

    else:

        print("No valid age data available.")

    # Category-wise Statistics

    categories = category_wise_statistics(data)

    print("\n---------- Department-wise Statistics ----------")

    for department, statistics in categories.items():

        print(f"\nDepartment: {department}")

        print(
            f"Record Count: "
            f"{statistics['record_count']}"
        )

        if statistics["average_salary"] is not None:

            print(
                f"Average Salary: "
                f"{statistics['average_salary']:.2f}"
            )

            print(
                f"Minimum Salary: "
                f"{statistics['minimum_salary']:.2f}"
            )

            print(
                f"Maximum Salary: "
                f"{statistics['maximum_salary']:.2f}"
            )


def main():

    data = load_data()

    if data:

        print_analysis(data)

    else:

        print("No data available for analysis.")


if __name__ == "__main__":
    main()