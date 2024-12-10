"""""
# Я попробовал сделать доп функцию, но не разобрался как правильно ее интегрировать
def check_zero_T(number):
    str_number = str(number)
    s = 0
    for i in range(len(str_number)):
        s += i
        for T in str_number[-1]:
            if T == "0":
                str_number = str_number.removesuffix("0")
                str_number = str_number.__add__("1")
        return str_number
"""

def get_multiplied_digits(number):
    str_number = str(number)
    s = 0
    for i in range(len(str_number)):
        s += i
        for T in str_number[-1]:
            if T == "0":
                str_number = str_number.removesuffix("0")
                str_number = str_number.__add__("1")

    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1::]))
    else:
        return int(str_number)
print("--------------------------------------------------------")
result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)

