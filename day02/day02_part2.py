sum_power = 0

biggest_green = 0 
biggest_red = 0
biggest_blue = 0

index_full = 0
pair = []
with open('day02_input.txt', 'r') as file:
    for line in file:
        array = line.split(":")
        games = array[1].split(";")
        for game in games:
            hand = game.split(",")
            hand = [newlines.rstrip('\n') for newlines in hand]
            for element in hand:
                pair.append(element)  
                pair = [sub[1:] for sub in pair]
                pair = [string.split(" ") for string in pair]
                pair = pair[0]
                for cube in pair:
                    match(pair[1]):
                        case 'green':
                            if(int(pair[0]) > biggest_green):
                                biggest_green = int(pair[0]) 
                        case 'blue':
                            if(int(pair[0]) > biggest_blue):
                                biggest_blue = int(pair[0])
                        case 'red':
                            if(int(pair[0]) > biggest_red):
                                biggest_red = int(pair[0])
                pair = []
        index_full +=1  
        # print(index_full, "green:", biggest_green, "red:", biggest_red, "blue:", biggest_blue)
        sum_power = (biggest_blue * biggest_green  * biggest_red) + sum_power
        print(sum_power, index_full)
        
        biggest_green = 0 
        biggest_red = 0
        biggest_blue = 0        