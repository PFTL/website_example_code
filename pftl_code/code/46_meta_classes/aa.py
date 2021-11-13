class Meta(type):
    def __new__(cls, name, bases, dict, **kwargs):
        print(name)
        print(bases)
        print(dict)
        print(kwargs)
        return super().__new__(cls, name, bases, dict)


class NewMeta:
    def __new__(cls, name, bases, dict, **kwargs):
        print(name)
        print(bases)
        print(dict)
        print(kwargs)
        return super().__new__(cls, name, bases, dict)


class MyClass(object, metaclass=Meta, kwarg='a', kwarg2='b'):
    pass

class MyNewClass(metaclass=Meta):
    pass

# mc = MyClass()
# print(type(MyClass))
# print(type(mc))

# mnc = MyNewClass()
# print(type(MyNewClass))