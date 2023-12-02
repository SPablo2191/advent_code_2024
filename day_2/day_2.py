import sys
import re
sys.path.append("..")  
from utils import read_document

def split_game(game : str) -> list[str]:
    """summary: split document line into list of strings"""
    return game.split(";")

def delete_spaces(result : str) -> str:
    """summary: delete spaces from string"""
    return result.replace(" ", "")

def check_game(results : list[str]) -> bool:
    cubes_options = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for result in results:
        type_result = result.strip().split(" ")
        if type_result[1] in cubes_options:
            if int(type_result[0]) > cubes_options[type_result[1]]:
                return False
        else:
            return False
    return True


def play_game():
    lines = read_document("data.txt")
    id_sum = 0
    games = [line.strip().split(": ") for line in lines]
    for game in games:
        game_id = int(game[0].split(" ")[1])
        print(f"Game #{game_id} is starting...")
        results = split_game(game[1])
        game_is_posible = True
        values =[result.strip().split(",") for result in results]
        for value in values:
            if not check_game(value):
                game_is_posible = False
                break
        if game_is_posible: 
            print(f"Game #{game_id} is possible")
            id_sum += game_id
        else:
            print(f"Game #{game_id} is not possible")
    print(f"Sum of possible games is {id_sum}")
    
        
    



def main():
    play_game()

if __name__ == "__main__":
    main()