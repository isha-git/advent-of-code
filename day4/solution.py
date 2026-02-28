#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 4 Solution

This script solves both parts of Day 4 of Advent of Code 2024.
It reads input from a file called input.txt and handles both parts of the problem.
"""

import re
from collections import defaultdict

def read_input(filename="input.txt"):
    """
    Read the input file and return its contents as a list of lines.
    
    Args:
        filename (str): Name of the input file. Defaults to "input.txt".
    
    Returns:
        list: List of lines from the input file.
    """
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def parse_card(line):
    """
    Parse a single card line into its components.
    
    Args:
        line (str): A line from the input file representing a card.
    
    Returns:
        tuple: (card_id, winning_numbers, numbers_you_have)
    """
    # Split the line into the card ID part and the numbers part
    card_part, numbers_part = line.split(":")
    card_id = int(re.search(r'\d+', card_part).group())
    
    # Split the numbers into winning numbers and numbers you have
    winning_numbers_part, numbers_you_have_part = numbers_part.split("|")
    winning_numbers = set(map(int, winning_numbers_part.split()))
    numbers_you_have = set(map(int, numbers_you_have_part.split()))
    
    return card_id, winning_numbers, numbers_you_have

def calculate_points(card):
    """
    Calculate the points for a single card based on matching numbers.
    
    Args:
        card (tuple): (card_id, winning_numbers, numbers_you_have)
    
    Returns:
        int: Points for the card.
    """
    _, winning_numbers, numbers_you_have = card
    matches = winning_numbers.intersection(numbers_you_have)
    
    if not matches:
        return 0
    
    return 2 ** (len(matches) - 1)

def solve_part1(cards):
    """
    Solve part 1 of the problem.
    
    Args:
        cards (list): List of parsed cards.
    
    Returns:
        int: Total points for all cards.
    """
    return sum(calculate_points(card) for card in cards)

def solve_part2(cards):
    """
    Solve part 2 of the problem.
    
    Args:
        cards (list): List of parsed cards.
    
    Returns:
        int: Total number of scratchcards after processing all wins.
    """
    # Initialize a dictionary to keep track of the number of copies for each card
    card_copies = defaultdict(int)
    
    for card in cards:
        card_id, winning_numbers, numbers_you_have = card
        matches = len(winning_numbers.intersection(numbers_you_have))
        
        # Add the original card to the count
        card_copies[card_id] += 1
        
        # For each copy of this card, add copies of the subsequent cards
        for i in range(card_copies[card_id]):
            for j in range(1, matches + 1):
                card_copies[card_id + j] += 1
    
    return sum(card_copies.values())

def main():
    """
    Main function to read input, solve both parts, and print the results.
    """
    lines = read_input()
    if not lines:
        return
    
    # Parse all cards
    cards = [parse_card(line) for line in lines]
    
    # Solve part 1
    part1_result = solve_part1(cards)
    print(f"Part 1: Total points = {part1_result}")
    
    # Solve part 2
    part2_result = solve_part2(cards)
    print(f"Part 2: Total scratchcards = {part2_result}")

if __name__ == "__main__":
    main()