class MyDescriptor:
    def __init__(self, fget=None, fset=None):
        print('Instantiating descriptor')
        self.fget = fget
        self.fset = fset

    def __set_name__(self, owner, name):
        if not hasattr(owner, '_descriptors'):
            setattr(owner, '_descriptors', [])

        owner._descriptors.append(name)

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
    _var1 = 1

    @MyDescriptor
    def var(self):
        return self._var

    @var.setter
    def var(self, value):
        self._var = value

    @MyDescriptor
    def var1(self):
        return self._var1


class MyOtherClass(MyClass):
    _new_var = 2

    @MyDescriptor
    def new_var(self):
        return self._new_var


my_class = MyClass()
my_other_class = MyOtherClass()
print(my_other_class.new_var)
print(my_class.var)
my_class.var = 5
print(my_class.var)

print(my_class._descriptors)
print(my_other_class._descriptors)


