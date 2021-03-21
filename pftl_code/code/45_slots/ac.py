class Person:
    birth_year = 1986
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_name(self):
        print(self.name)


if __name__ == '__main__':
    print(Person.__dict__)
    me = Person(35, 'Aquiles')
    print(me.__dict__)

    print(me.__dict__['name'])
