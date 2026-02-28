#!/usr/bin/env python3
"""
This script checks if a number is prime, even or odd, and whether it's less than 100.
"""

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

def main():
    """Main function to check number properties."""
    try:
        num = int(input("Enter a number: "))
        prime = is_prime(num)
        even = is_even(num)
        less_than_hundred = is_less_than_hundred(num)
        
        print(f"Number: {num}")
        print(f"Prime: {'Yes' if prime else 'No'}")
        print(f"Even: {'Yes' if even else 'No'}")
        print(f"Less than 100: {'Yes' if less_than_hundred else 'No'}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()