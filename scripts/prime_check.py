def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

def is_less_than_hundred(n):
    """Check if a number is less than 100."""
    return n < 100

def check_number(n):
    """Check properties of a number."""
    prime = is_prime(n)
    even = is_even(n)
    less_than_hundred = is_less_than_hundred(n)
    
    print(f"Number: {n}")
    print(f"Prime: {'Yes' if prime else 'No'}")
    print(f"Even: {'Yes' if even else 'No'}")
    print(f"Less than 100: {'Yes' if less_than_hundred else 'No'}")

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        check_number(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")