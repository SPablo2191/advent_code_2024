import sys
import string
sys.path.append("..") 
from utils import read_document
symbol_list = [symbol for symbol in string.punctuation if symbol != "."] # get list of symbols


def is_part_number(matrix, row, column) -> bool:
    global symbol_list
    # print(f"checking if {matrix[row][column]} is a part number... position: {row}, {column}")
    neighbors = []
    for i in range(row-1, row+2):
        for j in range(column-1, column+2):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and (i != row or j != column):
                neighbors.append(matrix[i][j])
    return any(element in symbol_list for element in neighbors)


def get_sum_part_numbers():
    lines = read_document("input.txt")
    lines_matrix = [list(line) for line in lines] # get matrix of symbols
    sum_parts = 0
    for i  in range(len(lines_matrix)):
        aux = ""
        for j  in range(len(lines_matrix[i])):
            if lines_matrix[i][j].isnumeric():
                aux += lines_matrix[i][j]
            else:
                if aux != "":
                    print(f"checking if {aux} is a part number...")
                    if is_part_number(lines_matrix, i,j):
                        print(f"{aux} is a part number!")
                        sum_parts += int(aux)
                    aux = ""
    print(f"The sum of all part numbers is {sum_parts}")



def main():
    get_sum_part_numbers()

if __name__ == "__main__":
    main()

