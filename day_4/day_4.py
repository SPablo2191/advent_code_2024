import sys
sys.path.append("..") 
from utils import read_document

def get_numbers(numbers : str) -> list[str]:
    """get the numbers of a card and return them as a list
    Keyword arguments:
    numbers -- string containing the numbers of the card
    Return: list of numbers
    """
    numbers = numbers.strip().split(' ')
    numbers = [int(number) for number in numbers if number != '' and number.isnumeric()]
    return numbers


def increase_points(current_value : int) -> int:
    if current_value == 0:
        return 1
    return current_value * 2

def sum_points_cards():
    """sum the points of the cards in the hand
    """
    lines = read_document('input.txt')
    total_points = 0
    for line in lines:
        card = line.split(":")
        card_id = card[0].split(" ")[1]
        card_numbers = card[1].split('|')
        winning_numbers = get_numbers(card_numbers[0])
        having_numbers = get_numbers(card_numbers[1])
        card_points = 0
        for number in winning_numbers:
            if number in having_numbers:
                card_points = increase_points(card_points)
        print(f"Card {card_id}: has {card_points} points.")
        total_points += card_points
    print(f"Part one: The total points are {total_points}")

def main():
    sum_points_cards()

if __name__ == "__main__":
    main()