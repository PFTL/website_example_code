class MyDescriptor:
    def __init__(self, fget, fset=None):
        print('Instantiating descriptor')
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        print('Getting Descriptor')
        return self.fget(instance)

    def __set__(self, instance, value):
        print('Setting Descriptor')
        self.fset(instance, value)

    def setter(self, fset):
        return type(self)(self.fget, fset)


class MyClass:
    _var = 0

    @MyDescriptor
    def var(self):
        return self._var

    @var.setter
    def var_setter(self, value):
        self._var = value


my_class = MyClass()
print(my_class.var)
my_class.var_setter = 2
print(my_class.var_setter)
print(my_class.var)