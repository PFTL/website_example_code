class MyClass:
    _var = 0

    def var_setter(self, value):
        self._var = value

    var = property(None, var_setter)

my_class = MyClass()
my_class.var = 2
print(my_class.var)