# Exercice 2.5
"""
Première approche sans split
"""

message1 = '1567:xhjuy:156:jukjl'
numeric = []

count = 0
flag = 0
while count < len(message1): 
    if message1[count].isdigit():
        numeric.append(message1[count]) 
        flag = 0
    
    if message1[count].isdigit() == False:
         flag += 1 

    if flag == 1:
         numeric.append(' ')


    count += 1

print("".join(numeric) )

# Deuxième solution en utilisant :
numeric = []
for m in message1.split(':'):
    if m.isdigit():
        numeric.append( int(m) )

print(numeric)

numeric = [ int(x) for x in message1.split(':') if x.isdigit()]

print(numeric)

message2 = '8790: bonjour le monde:8987:7777:Hello World:    9007'

numeric2 = []
for m in message2.split(':'):
    if m.strip().isdigit():
        numeric2.append( int(m) )

print(numeric2)

numeric2 = [ int(x) for x in message2.split(':') if x.strip().isdigit()]