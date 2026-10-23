
dataset = []
is_two_dimensional = False
dataset_summary = {"total": 0, "mean": 0}


def get_flat_data():
    """Creates a flat list from the stored dataset."""

    flat_data = []

    if is_two_dimensional:
        for row in dataset:
            for value in row:
                flat_data.append(value)
    else:
        for value in dataset:
            flat_data.append(value)

    return flat_data


def update_summary():
    """Updates the dataset summary information."""

    global dataset_summary

    flat_data = get_flat_data()

    dataset_summary = {
        "total": len(flat_data),
        "mean": sum(flat_data) / len(flat_data)
    }


def display_grid(grid):
    """Displays a 2D dataset in a formatted table."""

    for row in grid:
        line = ""

        for value in row:
            line += str(value).rjust(6)

        print(line)


def input_data():
    """Input a 1D list or 2D list manually, or use sample data."""

    global dataset, is_two_dimensional

    print("\n1. Enter 1D List")
    print("2. Enter 2D List")
    print("3. Sample 1D Data")
    print("4. Sample 2D Data")

    choice = input("Choose an option: ")

    if choice == "1":

        print("Enter values separated by spaces:")
        dataset = list(map(int, input().split()))
        is_two_dimensional = False

    elif choice == "2":

        rows = int(input("Enter number of rows: "))
        dataset = []

        for i in range(rows):
            print(f"Enter row {i + 1}:")
            row = list(map(int, input().split()))
            dataset.append(row)

        is_two_dimensional = True

    elif choice == "3":

        dataset = [34, 12, 56, 78, 43, 21, 90]
        is_two_dimensional = False

    elif choice == "4":

        dataset = [
            [34, 12, 56],
            [78, 43, 21],
            [90, 5, 67]
        ]

        is_two_dimensional = True

    else:
        print("Invalid choice.")
        return

    update_summary()

    print("\nData stored successfully!")

    if is_two_dimensional:
        display_grid(dataset)


def calculate_average(numbers):
    """Returns the average of all values."""

    return sum(numbers) / len(numbers)


def find_duplicates(numbers):
    """Finds duplicate values in a dataset."""

    duplicates = []

    for num in numbers:
        if numbers.count(num) > 1 and num not in duplicates:
            duplicates.append(num)

    return duplicates


def unique_values(numbers):
    """Returns all unique values."""

    unique_list = []

    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)

    return unique_list


def show_values(*values):
    """Displays values using *args."""

    print("Values:", end=" ")

    for item in values:
        print(item, end=" ")

    print()


def show_info(**details):
    """Displays dataset information using **kwargs."""

    print("Dataset Characteristics:")

    for key, value in details.items():
        print("-", key, ":", value)


def display_summary():
    """Display data summary using built-in functions."""

    flat_data = get_flat_data()

    print("\nData Summary:")
    print("- Total elements:", len(flat_data))
    print("- Minimum value:", min(flat_data))
    print("- Maximum value:", max(flat_data))
    print("- Sum of all values:", sum(flat_data))
    print("- Average value:", "%.2f" % calculate_average(flat_data))
    print("- Duplicates:", find_duplicates(flat_data))
    print("- Unique values:", unique_values(flat_data))

    print()

    show_values(*flat_data)

    show_info(
        type="2D" if is_two_dimensional else "1D",
        size=len(flat_data),
        total=dataset_summary["total"],
        mean="%.2f" % dataset_summary["mean"]
    )


def factorial(number):
    """Calculate factorial of a number using recursion."""

    if number <= 1:
        return 1

    return number * factorial(number - 1)


def fibonacci(position):
    """Return the nth Fibonacci number using recursion."""

    if position < 2:
        return position

    return fibonacci(position - 1) + fibonacci(position - 2)


def recursion_menu():

    number = int(input("Enter a number: "))

    print("\nFactorial of", number, "is:", factorial(number))

    print("Fibonacci Series:", end=" ")

    for i in range(number):
        print(fibonacci(i), end=" ")

    print()


def filter_data():

    threshold = int(input("Enter threshold value: "))

    mode = input(
        "1. Keep values >= threshold   2. Keep values < threshold : "
    )

    flat_data = get_flat_data()

    if mode == "2":

        filtered_data = list(
            filter(lambda x: x < threshold, flat_data)
        )

        print("\nFiltered Data (values <", threshold, "):")

    else:

        filtered_data = list(
            filter(lambda x: x >= threshold, flat_data)
        )

        print("\nFiltered Data (values >=", threshold, "):")

    print(filtered_data)

    doubled_values = list(
        map(lambda x: x * 2, filtered_data)
    )

    print("Doubled using map():", doubled_values)


def sort_data():

    global dataset

    print("\nChoose Sorting Option")
    print("1. Ascending")
    print("2. Descending")

    descending = input("Enter your choice: ") == "2"

    if is_two_dimensional:

        sorted_grid = []

        for row in dataset:
            sorted_grid.append(
                sorted(row, reverse=descending)
            )

        print("\nUsing sorted() (new list):")
        display_grid(sorted_grid)

        for row in dataset:
            row.sort(reverse=descending)

        print("Using sort() (original modified):")
        display_grid(dataset)

    else:

        print(
            "\nUsing sorted():",
            sorted(dataset, reverse=descending)
        )

        print("Original list:", dataset)

        dataset.sort(reverse=descending)

        print("Using sort() (in-place):", dataset)


def get_statistics(values):
    """Return minimum, maximum, total and average values."""

    return (
        min(values),
        max(values),
        sum(values),
        calculate_average(values)
    )


def display_statistics():

    minimum_value, maximum_value, total_value, average_value = \
        get_statistics(get_flat_data())

    print("\nDataset Statistics:")
    print("- Minimum value:", minimum_value)
    print("- Maximum value:", maximum_value)
    print("- Sum of all values:", total_value)
    print("- Average value:", "%.2f" % average_value)


def main():

    print("Welcome to the Data Analyzer and Transformer Program")

    while True:

        print("\nMain Menu")
        print("1. Input Data -", input_data.__doc__)
        print("2. Display Data Summary -", display_summary.__doc__)
        print("3. Calculate Factorial -", factorial.__doc__)
        print("4. Filter Data by Threshold")
        print("5. Sort Data")
        print("6. Display Dataset Statistics -", get_statistics.__doc__)
        print("7. Exit Program")

        choice = input("Please enter your choice: ")

        if choice == "7":

            print(
                "\nThank you for using the Data Analyzer and Transformer Program."
            )
            print("Goodbye!")
            break

        elif choice == "1":

            input_data()

        elif choice in ("2", "3", "4", "5", "6"):

            if choice == "3":

                recursion_menu()

            elif len(dataset) == 0:

                print("\nPlease input data first (Option 1).")

            elif choice == "2":

                display_summary()

            elif choice == "4":

                filter_data()

            elif choice == "5":

                sort_data()

            elif choice == "6":

                display_statistics()

        else:

            print("Invalid choice. Please try again.")


main()
