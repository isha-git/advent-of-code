#!/usr/bin/env python3
"""
A script to check if a number is prime, even or odd, and if it's less than 100.
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

def is_less_than_100(n):
    """Check if a number is less than 100."""
    return n < 100

def main():
    """Main function to check number properties."""
    try:
        num = int(input("Enter a number: "))
        print(f"Number: {num}")
        print(f"Is prime: {is_prime(num)}")
        print(f"Is even: {is_even(num)}")
        print(f"Is odd: {not is_even(num)}")
        print(f"Is less than 100: {is_less_than_100(num)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()