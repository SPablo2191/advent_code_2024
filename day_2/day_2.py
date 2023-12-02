import sys
sys.path.append("..")  
from utils import read_document

def split_game(game : str) -> list[str]:
    return game.split(";")

def play_game():
    games = read_document("data.txt")
    for game in games:
        game = split_game(game)
        print(game)

def main():
    play_game()

if __name__ == "__main__":
    main()