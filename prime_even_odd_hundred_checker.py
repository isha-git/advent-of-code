#!/usr/bin/env python3
"""
This script checks if a number is prime, even or odd, and whether it is less than 100.
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
    try:
        num = int(input("Enter a number: "))
        prime_status = "prime" if is_prime(num) else "not prime"
        even_odd_status = "even" if is_even(num) else "odd"
        hundred_status = "less than 100" if is_less_than_hundred(num) else "100 or more"
        print(f"The number {num} is {prime_status}, {even_odd_status}, and {hundred_status}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()