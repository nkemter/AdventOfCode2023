# 12 red cubes, 13 green cubes, and 14 blue cubes

import numpy as np
sum_green = 0
sum_red = 0
sum_blue = 0
sum_id = 0

max_green = 13
max_red = 12
max_blue = 14

index_full = 0
pair = []
tooBig = False
# with open('test.txt', 'r') as file:
with open('day02_input.txt', 'r') as file:
    for line in file:
        array = line.split(":")
        id = array[0].split(" ") #id[1] sind die id's
        games = array[1].split(";") #games[0] ist 1. mal zeigen | games[1] ist zweites zeigen ...
        for game in games:
            hand = game.split(",")
            hand = [newlines.rstrip('\n') for newlines in hand]
            for element in hand:
                value = element.split(" ")
                pair.append(element)  
                pair = [sub[1:] for sub in pair]
                pair = [string.split(" ") for string in pair]
                pair = pair[0]
                for hand in pair:
                    match(pair[1]):
                        case 'green':
                            if(int(pair[0]) > max_green):
                                tooBig = True
                        case 'blue':
                            if(int(pair[0]) > max_blue):
                                tooBig = True
                        case 'red':
                            if(int(pair[0]) > max_red):
                                tooBig = True
                pair = []
        index_full +=1  
        if(not tooBig):
            sum_id += index_full
        else:
            tooBig = False
        print(sum_id)