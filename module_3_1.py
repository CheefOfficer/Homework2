calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(*args):
    count_calls()
    for i in args:
        return len(i), str.upper(i), str.lower(i)

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in map(str.lower, list_to_search)

#_______________________________________________________________________
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Karamba'))
print(string_info('Deregable'))
print(is_contains("Urban", ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains("Good", ['od', 'Go', 'gooD']))
print(is_contains('HEAT', ['Cold', 'frosT']))
print(calls)
