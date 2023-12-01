from calibration import read_document


def get_calibration_value(word : str) -> int:
    calibration_value = []
    aux = ""
    for value in word:
        if value.isnumeric():
            calibration_value.append(value)
        else:
            aux += value
            if "one" in aux:
                calibration_value.append("1")
                aux = value
            elif "two" in aux:
                calibration_value.append("2")
                aux = value
            elif "three" in aux:
                calibration_value.append("3")
                aux = value
            elif "four" in aux:
                calibration_value.append("4")
                aux = value
            elif "five" in aux:
                calibration_value.append("5")
                aux = value
            elif "six" in aux:
                calibration_value.append("6")
                aux = value
            elif "seven" in aux:
                calibration_value.append("7")
                aux = value
            elif "eight" in aux:
                calibration_value.append("8")
                aux = value
            elif "nine" in aux:
                calibration_value.append("9")
                aux = value 
    return int(calibration_value[0] + calibration_value[-1])


def calculate_calibration_value_enhanced():
    document_lines : list[str] = read_document("document_enhanced.txt")
    total_sum : int = sum([get_calibration_value(line) for line in document_lines])
    print(f"The total sum is {total_sum}")

def main():
    calculate_calibration_value_enhanced()

if __name__ == "__main__":
    main()