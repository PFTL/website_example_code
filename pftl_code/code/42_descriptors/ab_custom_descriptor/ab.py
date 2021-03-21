class MyDescriptor:
    def __init__(self, fget):
        print('Instantiating descriptor')
        self.fget = fget

    def __get__(self, instance, owner):
        print('Getting Descriptor')
        return self.fget(instance)


class MyClass:
    _var = 0

    @MyDescriptor
    def var(self):
        print('Getting var')
        return self._var


my_class = MyClass()
print(my_class.var)

