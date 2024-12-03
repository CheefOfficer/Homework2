def get_password(bobber):
    password = ''
    for i in range(1, bobber):
        for j in range(2, bobber):
            if j <= i:
                continue
            if bobber % (i + j) == 0:
                password += str(i) + str(j)
    return password

n = int(input('Введите целое число от 3 до 20: '))

result = get_password(n)
print('Пароль:', result)

#выше - списал, а все что ниже я пытался сам...


"""""
import random
first_st = []
second_st = []
stounes = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
second_stounes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#def first_input():
#    random_stoune = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#    first_stoune = random.choice(random_stoune)
#    return first_stoune

def second_input():
    #random_stoune1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    second_stoune = random.choice(second_stounes)
    return second_stoune

def third_input():
    #random_stoune2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    third_stoune = random.choice(second_stounes)
    return third_stoune


length = 999#len(stounes)
i = -1
while i <= length:
    i += 1
    for n in stounes:
        j = second_input()
        k = third_input()
        p = j + k
        if n % p == 0:
          #  print(f'{n}', f'{p}')
            first_st.append(n), second_st.append(p)
        else:
            continue
otvet = {'левый камень': first_st, 'правый камень': second_st}
for key, value in otvet.items():
    print(f"{key}: {value}")

paired = list(zip(first_st, second_st))
sorted_pairs = sorted(paired)
sorted_list2 = [value for _, value in sorted_pairs]
print(sorted_list2)



#count = 0
#while count < 999:

#    count += 1

"""""
#for k in range(1, 99):
#    length = 999#len(stounes)
#    i = -1
#    while i <= length:
#        k=+1
#        print(first_st[k], second_st[k])
#
#    fstone = int(input("Введите номер на камне слева:   "))
#    if int(fstone) == first_st[k]:
#        print(second_st[k])
#    else:
#        continue

""""
#print (fstone in first_st)# проверить есть ли элемент в списке

#def code_database(n_range, p_range):
#    n_values = list[first_st]
#    p_values = list[second_st]

#    value_database = {
#        'N': n_values,
#        'P': p_values
#    }

#    return value_database

#fstone = int(input("Введите номер на камне слева:   "))
#print(code_database('N', 'P'))

#length = 999#len(stounes)
#i = -1
#while i <= length:
#    fstone = int(input("Введите номер на камне слева:   "))
#    i += 1
#    if fstone == ['N']:
#        print(['N'])

#    continue
"""




