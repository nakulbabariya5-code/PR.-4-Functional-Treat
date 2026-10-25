dataset = []
summary = {"total": 0, "mean": 0}

def refresh_summary():
    global summary
    if len(dataset) > 0:
        summary["total"] = len(dataset)
        summary["mean"] = sum(dataset) / len(dataset)

def input_data():
    global dataset
    print("\nStep 1: Input Data")
    print("Enter data for a 1D array (separated by spaces):")
    
    
    user_input = input()
    dataset = list(map(int, user_input.split()))
    
    refresh_summary()
    print("Data has been stored successfully!")

def avg(nums):
    return sum(nums) / len(nums)

def display_summary():
    print("\nStep 2: Display Data Summary ")
    print("\nData Summary:")
    print("- Total elements:", len(dataset))
    print("- Minimum value:", min(dataset))
    print("- Maximum value:", max(dataset))
    print("- Sum of all values:", sum(dataset))
    print("- Average value:", round(avg(dataset), 2))

def calc_factorial(n):
    if n <= 1:
        return 1
    return n * calc_factorial(n - 1)

def recursion_menu():
    print("\nStep 3: Calculate Factorial ")
    n = int(input("Enter a number to calculate its factorial: "))
    result = calc_factorial(n)
    print(f"Factorial of {n} is: {result}")

def filter_data():
    print("\nStep 4: Filter Data by Threshold ")
    limit = int(input("Enter a threshold value to filter out data above this value: "))
    
    filtered = list(filter(lambda x: x >= limit, dataset))
    
    print(f"\nFiltered Data (values >= {limit}):")
    print(", ".join(map(str, filtered)))

def sort_data():
    print("\nStep 5: Sort Data")
    print("Choose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    opt = input("Enter your choice: ")
    
    if opt == "2":
        sorted_lst = sorted(dataset, reverse=True)
        print("\nSorted Data in Descending Order:")
    else:
        sorted_lst = sorted(dataset)
        print("\nSorted Data in Ascending Order:")
        
    print(", ".join(map(str, sorted_lst)))

def get_stats(nums):
    return min(nums), max(nums), sum(nums), avg(nums)

def display_statistics():
    print("\nStep 6: Display Dataset Statistics (Return Multiple Values)")
    
    
    mn, mx, tot, avg_val = get_stats(dataset)
    
    print("\nDataset Statistics:")
    print("- Minimum value:", mn)
    print("- Maximum value:", mx)
    print("- Sum of all values:", tot)
    print("- Average value:", round(avg_val, 2))

def print_dataset_details(*args, **kwargs):
    """Dataset Characteristics: This function prints optional configurations and details."""
    
    print("\n--- Dataset Info Summary ---")
    if args:
        print("Additional Labels Provided:", args)
    if kwargs:
        print("Configuration Rules Applied:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

def main():
    print("Welcome to the Data Analyzer and Transformer Program")
    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary ")
        print("3. Calculate Factorial ")
        print("4. Filter Data by Threshold ")
        print("5. Sort Data")
        print("6. Display Dataset Statistics ")
        print("7. Print Dataset Details ")
        print("8. Exit Program")
        
        choice = input("Please enter your choice: ")
        
        if choice == "8":
            print("\nStep 7: Exit Program")
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
            
        if choice in ["2", "3", "4", "5", "6", "7"] and len(dataset) == 0:
            print("\nPlease input data first (Option 1).")
            continue
            
        if choice == "1":
            input_data()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            recursion_menu()
        elif choice == "4":
            filter_data()
        elif choice == "5":
            sort_data()
        elif choice == "6":
            display_statistics()
        elif choice == "7":
            print(print_dataset_details.__doc__)
            print_dataset_details("Numeric Collection", "1D Array", type="Integer", length=len(dataset))
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
