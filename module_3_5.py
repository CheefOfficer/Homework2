def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1::]))
    else:
        return int(str_number)
print("--------------------------------------------")
result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(4020301)
print(result2)
result2 = get_multiplied_digits(40231)
print(result2)
