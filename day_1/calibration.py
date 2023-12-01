def read_document(file_name : str) -> list[str]:
    with open(file_name, "r") as f:
        return f.readlines()

def get_calibration_value(word : str) -> int:
    aux = [value for value in word if value.isnumeric()]
    return int(str(aux[0])+str(aux[-1]))

def calculate_calibration_value():
    document_lines : list[str] = read_document("document.txt")
    total_sum : int = sum([get_calibration_value(line) for line in document_lines])
    print(f"The total sum is {total_sum}")


def main():
    calculate_calibration_value()

if __name__ == "__main__":
    main()