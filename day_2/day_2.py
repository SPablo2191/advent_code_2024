import sys
sys.path.append("..")  
from utils import read_document

def split_game(game : str) -> list[str]:
    """summary: split document line into list of strings"""
    return game.split(";")

def delete_spaces(result : str) -> str:
    """summary: delete spaces from string"""
    return result.replace(" ", "")

def play_game():
    cubes_options = ['red', 'green', 'blue']
    games = read_document("data.txt")
    red_cube_qty = int(input("How many red cubes? :"))
    green_cube_qty = int(input("How many green cubes? :"))
    blue_cube_qty = int(input("How many blue cubes? :"))
    id_sum = 0
    for game in games:
        game = split_game(game)
        red_cube_total = 0
        green_cube_total = 0
        blue_cube_total = 0
        for results in game:
            result = delete_spaces(results)
            if cubes_options[0] in result:
                red_cube_total += int(result[result.find(cubes_options[0])-1])
            if cubes_options[1] in result:
                green_cube_total += int(result[result.find(cubes_options[1])-1])
            if cubes_options[2] in result:
                blue_cube_total += int(result[result.find(cubes_options[2])-1])
        if red_cube_total <= red_cube_qty and green_cube_total <= green_cube_qty and blue_cube_total <= blue_cube_qty:
            id_sum += int(game[0][game[0].find(":")-1])
            print(f"Game {game[0][game[0].find(':')-1]} is possible")
    print(f"Sum of possible games (ID´s) is {id_sum}")


def main():
    play_game()

if __name__ == "__main__":
    main()