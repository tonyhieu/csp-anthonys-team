def ageChange(age1, age2):
    #print(age1, age2)
    if (age1 > age2):
        num = age1
        age1 = age2
        age2 = num
    return age1,age2
print( ageChange(16, 21) )
print ( ageChange(21, 16) )


matrix = [ [1,2,3],[4,5,6],[7,8,9] ]

for num2 in matrix:
    for num1 in num2:
        print (num1, end=" ")
    print()

