
# Première version
s = 0
for a in range(1000):
    if a % 5 == 0 or a % 3 ==0 :
        s += a 

print(s)

# Deuxième version Pythonique en partant de 1 jusqu'à 1000 inclu 

s2 = sum(num for num in range(1,1001) if num % 5 == 0 or num % 3 == 0 )

# faire la somme des termes d'une liste numérique
s3 = sum([6,7,8])

# somme des termes numériques de 1 à 10
s4 = sum (x for x in range(1,11))