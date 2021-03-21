class Person:
    __slots__ = 'age', 'name', '__dict__'

    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.birth_year = 1986

    def print_name(self):
        print(self.name)


if __name__ == '__main__':
    me = Person(35, 'Aquiles')
    print(me.__dict__)
    print(me.birth_year)
    me.new_var = 10
    print(me.__dict__)


