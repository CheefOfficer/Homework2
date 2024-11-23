first = int(input("Type first number: "))
second = int(input("Type second number: "))
third = int(input("Type third number: "))
if first == second and first == third:
    print("Number of same digits: 3")
elif first == second or second == third or first == third:
    print("Number of same digits: 2")
else:
    print("Number of same digits: 0")

#first = int(input("Type first number: "))
#second = int(input("Type second number: "))
#third = int(input("Type third number: "))
#if first == second and first == third:
#    print("Number of same digits: 3")
#elif first == second or second == third or first == third:
#    print("Number of same digits: 2")
#elif first != second or second != third or first != third:
#    print("Number of same digits: 0")
