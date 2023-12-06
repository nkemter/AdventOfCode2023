from datetime import datetime
start = datetime.now()
time = ['41968894']
distance = ['214178911271055']
# time = ['7','15','30']
# distance = ['9', '40', '200']
stragie_mult = 1

for index,zeit in enumerate(time):
    laden = 0
    strecke_in_zeit = 0
    stragie = 0
    for _ in range(int(zeit)):
        if int(distance[index]) < ((int(zeit) - laden) * strecke_in_zeit): 
            stragie += 1
        strecke_in_zeit += 1 
        laden += 1
    stragie_mult *= stragie 
print(stragie_mult)
print(datetime. now() - start)