
scores = [11, 89, 9, 90, 7, 190, 78, 200, 78, 13]

m = max(scores)
pos = 0

for i, num in enumerate(scores):
    if num == m:
        pos = i

print("Max: {}, position : {}".format(num, pos))

# En une ligne ! Attention il fait le max par rapport à la première valeur 
# dans le tuple (s,i) sur s 
print( max((scores[i], i) for i in range(len(scores))) )

print( [(x, i) for i, x in enumerate(scores) if max(scores) == x])


m = max(scores)
pos = scores.index(m)