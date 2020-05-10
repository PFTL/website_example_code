class MyClass:
    _var = 0

    @property
    def var(self):
        print('Getting Var')
        return self._var


my_class = MyClass()
print(my_class.var)