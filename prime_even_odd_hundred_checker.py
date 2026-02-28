def check_number(n):
    """Check if a number is prime, even/odd, and if it's less than 100."""
    
    # Check if the number is even or odd
    if n % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    
    # Check if the number is less than 100
    less_than_hundred = n < 100
    
    # Check if the number is prime
    if n <= 1:
        is_prime = False
    elif n == 2:
        is_prime = True
    else:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
    
    return {
        "number": n,
        "even_odd": even_odd,
        "less_than_hundred": less_than_hundred,
        "is_prime": is_prime
    }

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        result = check_number(num)
        print(f"\nResults for {result['number']}:")
        print(f"- Even/Odd: {result['even_odd']}")
        print(f"- Less than 100: {'Yes' if result['less_than_hundred'] else 'No'}")
        print(f"- Prime: {'Yes' if result['is_prime'] else 'No'}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")