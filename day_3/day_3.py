import sys
import string
sys.path.append("..") 
from utils import read_document
symbol_list = [symbol for symbol in string.punctuation if symbol != "."] # get list of symbols


def is_part_number(matrix, row, column) -> bool:
    global symbol_list
    neighbors = get_neighbors(matrix, row, column)
    # print(f"neighbors of {matrix[row][column]}: {neighbors}")
    return any(element in symbol_list for element in neighbors)

def get_neighbors(matrix, row, column):
    neighbors = []
    for i in range(row-1, row+2):
        for j in range(column-1, column+2):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and (i != row or j != column):
                neighbors.append(matrix[i][j])
    return neighbors

def is_a_gear(matrix, row, column) -> bool:
    neighbors = get_neighbors(matrix, row, column)
    print(f"the neighbors are: {neighbors}")
    parts_adjacent_numbers = [element for element in neighbors if element.isnumeric()]
    print(parts_adjacent_numbers)
    return len(parts_adjacent_numbers) >= 2
    

def get_sum_gear_ratios():
    lines = read_document("input.txt")
    lines_matrix = [list(line) for line in lines] # get matrix of symbols
    print(lines_matrix)
    for lines in lines_matrix:
        print(lines)
    
         
    


def get_sum_part_numbers():
    lines = read_document("input.txt")
    lines_matrix = [list(line) for line in lines] # get matrix of symbols
    sum_parts = 0
    for i  in range(len(lines_matrix)):
        aux = ""
        cont_part_number = 0
        for j  in range(len(lines_matrix[i])):
            if lines_matrix[i][j].isnumeric():
                if is_part_number(lines_matrix, i,j):
                    cont_part_number += 1
                aux += lines_matrix[i][j]
            else:
                if cont_part_number > 0:
                    print("valid part number: ", aux)
                    sum_parts += int(aux)
                    cont_part_number = 0
                elif (cont_part_number == 0) and (aux != ""):
                    print("invalid part number: ", aux)
                aux = ""
    print(f"The sum of all part numbers is {sum_parts}")



def main():
    get_sum_part_numbers()
    get_sum_gear_ratios()

if __name__ == "__main__":
    main()

