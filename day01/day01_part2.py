# https://adventofcode.com/2023/day/1


    
    
numbers = []
word = ""
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
line_value = 0
calibbration_values = 0

def word_is_digit(char):
    # print(digits)
    word = word + char
    print(word)
    for number in digits:
        if number in word:
            print("contains")
            word = ''
    #char wird übergeben und in array. wenn alle 9 wörter nicht stimmen 
    #return True oder so

# with open('day01_input.txt', 'r') as file:
with open('test.txt', 'r') as file:
    for line in file: #für jede zeile
        print(line, end="")
        line_value = 0
        numbers = []
        for char in line: #char einer zeile
            if char.isdigit(): # ob char eine zahl ist
                numbers.append(int(char))
            if word_is_digit(char):
                word = word_is_digit(char)
                print("zahl")
        #wenn zeile zu ende ist, dann werte addieren
        line_value = int(str(numbers[0]) + str(numbers[-1]))
        print(line_value, end="")
        calibbration_values += line_value
        print("\n")
    print("calibbration_values", calibbration_values)
    


        