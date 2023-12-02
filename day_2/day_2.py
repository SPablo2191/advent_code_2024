import sys
import re
sys.path.append("..")  
from utils import read_document
red_cube_qty = 1
green_cube_qty = 1
blue_cube_qty = 1


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

def set_red_power(value : int):
    global red_cube_qty
    if(red_cube_qty < value):
        red_cube_qty = value

def set_green_power(value : int):
    global green_cube_qty
    if(green_cube_qty < value):
        green_cube_qty = value

def set_blue_power(value : int):
    global blue_cube_qty
    if(blue_cube_qty < value):
        blue_cube_qty = value

def check_power(results : list[str]) -> bool:
    cubes_options = {
        "red": set_red_power,
        "green": set_green_power,
        "blue": set_blue_power
    }
    for result in results:
        type_result = result.strip().split(" ")
        if type_result[1] in cubes_options:
            cubes_options[type_result[1]](int(type_result[0]))




def play_game():
    global red_cube_qty, green_cube_qty, blue_cube_qty
    lines = read_document("data.txt")
    id_sum = 0
    power_sum = 0
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
            check_power(value)
        print(f"Game #{game_id}´s power => { red_cube_qty * green_cube_qty * blue_cube_qty}")
        power_sum += red_cube_qty * green_cube_qty * blue_cube_qty
        red_cube_qty = 0
        green_cube_qty = 0
        blue_cube_qty = 0
        if game_is_posible: 
            print(f"Game #{game_id} is possible")
            id_sum += game_id
        else:
            print(f"Game #{game_id} is not possible")
    print(f"PART 1: Sum of possible games is {id_sum}")
    print(f"PART 2: Sum of power is {power_sum}")
    
        
    



def main():
    play_game()

if __name__ == "__main__":
    main()