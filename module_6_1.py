class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_flor):
        if int(new_flor) > self.number_of_floors or int(new_flor) < 1:
            print(f'Такого ({new_flor}) этажа не существует')
        else:
            i = 1
            while i  < new_flor:
                print(i)
                i += 1
            print(new_flor)

h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(5)

h2.go_to(10)