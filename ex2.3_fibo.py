

a, b = 1, 1
fibo = [1, 1]

# _ rien sortir dans l'itération
for _ in range(1000):
    a, b = b, a + b 
    fibo.append(b)

#print(fibo)


""" 
Approche avec une technique particulière "récurrence"
compter par exemple les permutations de 10 objets 
par exemple si on a 3 personnages p1, p2, p3 on peut compter 
les permutations de ces 3 personnages : 3! = 3*2*1 

Pour 10 personnages :
10! = 10*9*8*7*6*5*4*3*2*1

"""

"""
    factoriel(3)
    3*factoriel(2)
    3*2*factoriel(1)
    3*2*1

"""
def factoriel(n):
    if n == 1:
        return 1
    else:
        return n*factoriel(n-1)


print(factoriel(5))

import sys 

sys.setrecursionlimit(3000)

def fiboRec(l=[1, 1]):

    if len(l) == 1000:
        return l 

    else:
        l.append(l[-2] + l[-1])

        return fiboRec(l)


print(fiboRec())




