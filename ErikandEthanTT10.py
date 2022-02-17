age1 = 21
age2 = 16

print(age1, age2)

if (age1 > age2):
    temp = age1
    age1 = age2
    age2 = temp

print(age1, age2)

print("")

matrix = [ [1,2,3],[4,5,6],[7,8,9] ]

for num in matrix:
    for isaac in num:
        print(isaac, end=" ")
    print()