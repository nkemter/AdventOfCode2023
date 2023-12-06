numbers = []
line_value = 0
calibration_values = 0
with open('day01_input.txt', 'r') as file:
    for line in file:
        print(line, end="")
        line_value = 0
        numbers = []
        for char in line: 
            if char.isdigit():
                numbers.append(int(char))
        line_value = int(str(numbers[0]) + str(numbers[-1]))
        calibration_values += line_value
    print("calibbration_values", calibration_values)