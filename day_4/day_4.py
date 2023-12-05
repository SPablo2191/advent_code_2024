import sys
sys.path.append("..") 
from utils import read_document


def sum_points_cards():
    """sum the points of the cards in the hand
    """
    lines = read_document('input.txt')
    for line in lines:
        card = line.split(":")
        card_id = card[0][-1]
        card_numbers = card[1].split('|')
        winning_numbers = card_numbers[0].strip().split(' ')
        having_numbers = card_numbers[1].strip().split(' ')
        print(having_numbers)

def main():
    sum_points_cards()

if __name__ == "__main__":
    main()