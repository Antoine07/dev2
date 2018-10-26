# Exercice II.2

matrix = [
    [1100, 1990, 1989, 1879],
    [2052, 2008, 2052, 2024],
    [1907, 1210, 220, 1200],
    [1100, 1990, 1989, 1879],
    [2052, 2008, 2052, 2024],
    [2032, 2020, 2056, 2032],
    [1100, 1990, 1989, 1879],
    [2052, 2008, 2052, 2024],
    [1907, 1210, 220, 1200],
    [1100, 1990, 1989, 1879],
    [2052, 2008, 2052, 2024],
    [1907, 1210, 220, 1200],
]

maskBissextile = {}

for i, line in enumerate(matrix):
    for year in line:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) :
            maskBissextile[i] = True
        else:
            maskBissextile[i] = False
            break # pensez à faire ce break

print(maskBissextile)


# Exercice deuxième correction

print( all( [True, True, False] ) ) # False

print( all( [True, True, True] ) ) # True


print( all(x > 0 for x in [1, 10, 9, 10]))

print(all( x % 2 == 0  for x in [10, 2, 4, 8])) # True car tous les éléments sont vraies


maskBissextile = {}

for i, line in enumerate(matrix):
    maskBissextile[i] = all(
        ( year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) )
        for year in line
    )

print(maskBissextile)