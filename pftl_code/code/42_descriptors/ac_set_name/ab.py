class MyDescriptor:
    def __init__(self, fget=None, fset=None):
        print('Instantiating descriptor')
        self.fget = fget
        self.fset = fset

    def __set_name__(self, owner, name):
        print(f'Setting name to {name}')
        if not hasattr(owner, '_descriptors'):
            setattr(owner, '_descriptors', [])

        owner._descriptors.append(name)


class MyClass:
    _var = 0
    _var1 = 0

    @MyDescriptor
    def var(self):
        return self._var

    @MyDescriptor
    def var1(self):
        return self._var1


my_class = MyClass()
print(my_class._descriptors)
print(my_class.var.fget(my_class))