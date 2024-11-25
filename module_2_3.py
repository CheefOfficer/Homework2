my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
length = len(my_list)
i = -1
while i <= length:
    i +=1
    if int(my_list[i]) < 0:
        break
    elif int(my_list[i]) > 0:
        print(my_list[i])
        continue

