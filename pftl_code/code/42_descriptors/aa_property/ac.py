class MyClass:
    _var = 0

    @property
    def var(self):
        print('Getting var')
        return self._var

    @var.setter
    def var(self, value):
        print('Setting var')
        if not isinstance(value, int):
            raise TypeError('Value must be integer')
        self._var = value


my_class = MyClass()
print(my_class.var)
my_class.var = 2.0
print(my_class.var)