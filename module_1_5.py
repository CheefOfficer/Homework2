immutable_var = (1, 2, 'string', True, 4)
print("Immutable var:", immutable_var)
#immutable_var[2] = 3
#TypeError: 'tuple' object does not support item assignment
#элементы кортежа не могут быть изменены в связи с тем, что это не поддерживается, кортежы неизменяемы
mutable_list = [1, 'trank', 5, 3, 2]
mutable_list[1] = 9
print("Mutable list:", mutable_list)