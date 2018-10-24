# Exercice II.1

s = 'mississippi'
letters = set(s)
d = {}

for l in letters:
    d[l] = 0
    for c in s :
        if c == l:
            d[l] += 1 

# deuxième solution plus optimise
# print(d)

s = 'mississippi'
d = {}

# retournera la liste des lettres qu'une fois propre à un set ou ensemble
letters = set(s)

for ch in letters:
    d[ch] = 0  # d = { 'm' : 0 }
    for l in s:
        if l == ch:
            d[ch] +=1 

print(d) 