data = [(1,2,6,7,8,11), (7,2,10,17,9,121),(0,8,9,6)]

evens = []
odds = []
for vect in data:
    for num in vect:
        if num in evens or num in odds:
            continue
        if num %2 ==0:
            evens.append(num)
        else:
            odds.append(num)

print(evens)

evens2 = [ num for vect in data for num in vect if num % 2 ==0 ]
# set crée un ensemble or le propre d'un ensemble c'est d'avoir un représentant
# unique de chaque élément => vire les doublons 
# list transforme un set en list
evens2 = list( set( evens2) )
print( evens2 )