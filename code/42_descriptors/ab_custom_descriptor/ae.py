class MyDescriptor:
    def __init__(self, fget=None, fset=None, val_min=None, val_max=None):
        print('Instantiating descriptor')
        self.val_min = val_min
        self.val_max = val_max
        self.fget = fget
        self.fset = fset

    def __call__(self, fget):
        return type(self)(fget, self.fset, self.val_min, self.val_max)

    def __get__(self, instance, owner):
        print('Getting Descriptor')
        return self.fget(instance)

    def __set__(self, instance, value):
        print('Setting Descriptor')
        if not self.val_min <= value <= self.val_max:
            raise ValueError(f'Value must be between {self.val_min} and {self.val_max}')
        self.fset(instance, value)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.val_min, self.val_max)


class MyClass:
    _var = 0

    @MyDescriptor(val_min=0, val_max=3)
    def var(self):
        return self._var

    @var.setter
    def var(self, value):
        self._var = value


my_class = MyClass()
print(my_class.var)
my_class.var = 5
print(my_class.var)