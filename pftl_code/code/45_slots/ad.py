class Person:
    __slots__ = 'age', 'name'
    birth_year = 1986

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_name(self):
        print(self.name)


if __name__ == '__main__':
    me = Person(35, 'Aquiles')
    print(type(Person.__dict__['birth_year']))
    print(type(Person.__dict__['age']))


