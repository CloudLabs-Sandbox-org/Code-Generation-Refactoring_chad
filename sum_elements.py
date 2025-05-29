"""Program to calculate sum of user-provided integers.

This module provides functionality to accept a series of integers from the user
and calculate their sum while handling various error cases.
"""

from typing import List

# Constants
MAX_ELEMENTS = 100
MIN_ELEMENTS = 1

def validate_input_count(count: int) -> bool:
    """Validate if the input count is within acceptable range.

    Args:
        count (int): Number of elements to be summed

    Returns:
        bool: True if count is valid, False otherwise
    """
    return MIN_ELEMENTS <= count <= MAX_ELEMENTS

def calculate_sum(numbers: List[int]) -> int:
    """Calculate the sum of all numbers in the list.

    Args:
        numbers (List[int]): List of integers to sum

    Returns:
        int: Sum of all numbers
    """
    return sum(numbers)

def get_user_numbers(count: int) -> List[int]:
    """Get specified number of integers from user input.

    Args:
        count (int): Number of integers to collect

    Returns:
        List[int]: List of collected integers

    Raises:
        ValueError: If user enters non-integer input
    """
    print(f"\nEnter {count} integers (one per line):")
    return [int(input(f"Number {i+1}: ")) for i in range(count)]

def main() -> None:
    """Main function to run the program."""
    try:
        # Get number of elements
        input_str = input(f"Enter the number of elements ({MIN_ELEMENTS}-{MAX_ELEMENTS}): ")
        count = int(input_str)

        if not validate_input_count(count):
            print(f"Error: Please enter a number between {MIN_ELEMENTS} and {MAX_ELEMENTS}.")
            return

        # Get numbers and calculate sum
        try:
            numbers = get_user_numbers(count)
            total = calculate_sum(numbers)
            print(f"\nSum of the numbers: {total}")

        except ValueError:
            print("Error: Please enter valid integers only.")
            return

    except ValueError:
        print("Error: Please enter a valid integer for the count.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
