# https://adventofcode.com/2023/day/1

numbers = []
line_value = 0
calibbration_values = 0
with open('day01_input.txt', 'r') as file:
    for line in file: #für jede zeile
        print(line, end="")
        line_value = 0
        numbers = []
        for char in line: #char einer zeile
            if char.isdigit(): # ob char eine zahl ist
                numbers.append(int(char))
        #wenn zeile zu ende ist, dann werte addieren
        line_value = int(str(numbers[0]) + str(numbers[-1]))
        print(line_value, end="")
        calibbration_values += line_value
        print("\n")
    print("calibbration_values", calibbration_values)
        