"""Card drawing program that simulates drawing cards from a standard deck."""
from typing import List, Tuple
import itertools
import random

def create_deck() -> List[Tuple[str, str]]:
    """Create a standard deck of 52 playing cards.
    
    Returns:
        List[Tuple[str, str]]: List of (value, suit) card tuples
    """
    values = {
        1: 'Ace',
        11: 'Jack',
        12: 'Queen',
        13: 'King'
    }
    suits = ['Spade', 'Heart', 'Diamond', 'Club']
    
    deck = []
    for num, suit in itertools.product(range(1, 14), suits):
        value = values.get(num, str(num))
        deck.append((value, suit))
    return deck

def draw_cards(deck: List[Tuple[str, str]], num_cards: int = 5) -> List[Tuple[str, str]]:
    """Draw a specified number of cards from the deck.
    
    Args:
        deck (List[Tuple[str, str]]): Deck of cards to draw from
        num_cards (int, optional): Number of cards to draw. Defaults to 5.
    
    Returns:
        List[Tuple[str, str]]: List of drawn cards
    
    Raises:
        ValueError: If attempting to draw more cards than available
    """
    if num_cards > len(deck):
        raise ValueError(f"Cannot draw {num_cards} cards from a deck of {len(deck)} cards")
    return deck[:num_cards]

def main():
    """Main function to run the card drawing program."""
    try:
        # Create and shuffle the deck
        deck = create_deck()
        random.shuffle(deck)

        # Draw and display cards
        drawn_cards = draw_cards(deck)
        print("\nYou got:")
        for card in drawn_cards:
            print(f"{card[0]} of {card[1]}s")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
