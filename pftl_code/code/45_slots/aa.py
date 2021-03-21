class Person:
    __slots__ = 'name', 'last_name'
    age = 35

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    me = Person('Aquiles')
    print(me.name)
    me.name = 'John'
    print(me.name)
    me.last_name = 'Doe'
    print(me.last_name)
    print(me.age)
    me.age = 50
    print(me.age)