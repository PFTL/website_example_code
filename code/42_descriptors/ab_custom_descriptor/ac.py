class MyDescriptor:
    def __init__(self, fget):
        print('Instantiating descriptor')
        self.fget = fget

    def __get__(self, instance, owner):
        print('Getting Descriptor')
        return self.fget(instance)

    def __set__(self, instance, value):
        raise Exception('This is a read-only descriptor')


class MyClass:
    _var = 0

    @MyDescriptor
    def var(self):
        return self._var


my_class = MyClass()
print(my_class.var)
my_class.var = 2
print(my_class.var)