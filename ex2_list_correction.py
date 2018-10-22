data = [(1,2,'H',6,7,8,11), (7,2,10,'A',17,9,'R',121),(0,8,'R',9,6, 'Y')]

name = ''
for v in data:
    for num in v:
        if str(num).isdigit() == False:
            name += str(num)

print(name)

print("".join(ch for vect in data for ch in vect if str(ch).isdigit() == False))