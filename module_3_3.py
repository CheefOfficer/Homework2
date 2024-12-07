def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 1.5, b = 'string', c = False)
print_params(a = 0.4)
print_params(c = True)
print_params(b = 25)
print_params(c = [1,2,3])
print("-------------------------------------")
values_list = [1, 'string', True]
values_dict = {'a' : 1234, 'b' : 'строка', 'c' : True}
print_params(*values_list)
print_params(**values_dict)
print("-------------------------------------")
values_list_2 = [1, 'string']
print_params(*values_list_2, 42)



