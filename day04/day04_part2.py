with open('day04_input.txt', 'r') as file:
    games_anzahl = [1] * 6
    index = 0
    for line in file:
        array = line.split(":")[1].split("|")
        array = [newlines.rstrip('\n') for newlines in array]
        array = [sub[1:] for sub in array]
        array = [string.split(" ") for string in array]
        array[0] = list(filter(None, array[0])) 
        array[1] = list(filter(None, array[1]))
        point = 0
        for element in array[1]: # jede gewinner nummer wird verglichen
            if element in array[0]:                                 # wenn ich "gewinne"
                point += 1
                games_anzahl[index + point] += games_anzahl[index]  # ich gehe von meinem aktuellen spiel (index) die punkte (points) weiter, die ich gerade habe
                                                                    # dann rechne ich die alten werte dieser karte + den wert meiner aktuellen karte 
                                                                    # (weil so oft habe ich die aktuellekarte ja, also erhalte ich ja auch so oft die kopie), 
                                                                    # um die neue anzahl der "weitergegangen karte" zu erhalten
                print(element, games_anzahl[index + point], games_anzahl[index])
        index += 1 
    print(sum(games_anzahl))