# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53 -> 8 punkte -> 1, 2, 4, 8
# with open('test.txt', 'r') as file:
with open('day04_input.txt', 'r') as file:
    total_points = 0
    for line in file:
        array = line.split(":")[1].split("|")
        array = [newlines.rstrip('\n') for newlines in array]
        array = [sub[1:] for sub in array]
        array = [string.split(" ") for string in array]
        array[0] = list(filter(None, array[0])) #macht leere strings weg
        array[1] = list(filter(None, array[1]))
        # print(array)

        for element in array[0]:
            index = 0
            mult = 0
            points = 0
            contained = [a in array[1] for a in array[0]]
            for bool in contained:
                if bool: 
                    if points == 0:
                        points = 1

                    else:
                        points = points * 2
        total_points += points
    print(total_points)
            
