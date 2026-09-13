# Exception Handling


try:

    number = int(input("Enter a number: "))

    result = 100 / number

    print("Result:", result)


except ValueError:

    print("Invalid input. Please enter a number.")


except ZeroDivisionError:

    print("Cannot divide by zero.")


except Exception as error:

    print("Unexpected error:", error)


finally:

    print("Program execution completed.")