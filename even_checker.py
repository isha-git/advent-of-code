def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        if is_even(num):
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")