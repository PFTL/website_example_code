class MyClass:
    _var = 0

    @property
    def var(self):
        print('Getting var')
        return self._var

    @var.setter
    def var(self, value):
        print('Setting var')
        self._var = value


my_class = MyClass()
print(my_class.var)
my_class.var = 2
print(my_class.var)