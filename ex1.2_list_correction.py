
len("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


phrases = [
    'Beautiful is better than ugly', 'Explicit is better than implicit.',
    'Simple is better than complex.', 'Complex is better than complicated.',
    'In the face of ambiguity, refuse the temptation to guess.',
    'Complex is better than complicated.', 'Sparse is better than dense.',
    'Readability counts.', 'Special cases aren t special enough to break the rules.',
    'Now is better than never.', 
    'Although practicality beats purity.', 'Errors should never pass silently.',
    'Unless explicitly silenced.', 
]

candidatLength = 0
candidate = { 'phrase' : '', 'pos' : 0, 'len' : 0}

for i, phrase in enumerate(phrases):
    if len(phrase) > candidatLength :
        candidatLength = len(phrase)
        candidate['phrase'] = phrase
        candidate['pos'] = i
        candidate['len'] = candidatLength

# print(candidate)

phraseStat = [(phrase, pos, len(phrase)) 
for pos, phrase in enumerate(sorted(phrases, key=len, reverse=True)) ]

print(phraseStat[0])


# Meme référence de liste pas de copie car une liste est un objet
l = [7,11,8,2,90]

l2  = l
l2.append(77)

print(l)
print(l2)

l3 = l[:] # shallow copy crée une nouvelle liste
l3.append(66)

print(l)
print(l3)

# vraie copie 

a = 7
b = a 

b = 11
print("a : {} b :{}".format(a, b))




