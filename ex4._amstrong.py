nombres_armstrong = []

nb_str = ""

for number in range(1000):
    nb_str = str(number)
    if len(nb_str) == 1:
        temp = number**3
        if temp == number:
            nombres_armstrong.append(temp)
    if len(nb_str) == 2:
        temp = int(nb_str[0])**3 + int(nb_str[1])**3
        if temp == number:
            nombres_armstrong.append(temp) 
    if len(nb_str) == 3:
        temp = int(nb_str[0])**3 + int(nb_str[1])**3 + int(nb_str[2])**3
        if temp == number:
            nombres_armstrong.append(temp)

print(nombres_armstrong)

# Exercice correction dev2 faites ensemble
def sumPowerThree(number):
    r = number 
    s = 0
    while number != 0:
        r = number % 10
        s += r**3
        number = number // 10

    return s

print(sumPowerThree(153))

amstrong = [ num for num in range(2, 100000) 
if sumPowerThree(num) == num  ]

print(amstrong)




