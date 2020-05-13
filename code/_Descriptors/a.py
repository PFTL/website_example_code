class Descriptor:
    def internal_method(self):
        print(self.value)

    def __set_name__(self, owner, name):
        print(f'Setting Name {owner}, {name}')
        self.name = name
        self.owner = owner

    def __set__(self, instance, value):
        self.value = value
        print('Setting')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        print('getting')
        return self #instance.__dict__[self.name]


class MyClass:
    descriptor = Descriptor()

    @property
    def my_prop(self):
        return 1

    @my_prop.setter
    def my_prop(self, val):
        self.val = 2


mc = MyClass()
mcc = MyClass()
mc.my_prop = 2
mc.descriptor = 3
print(mc.__dict__)
print(mcc.__dict__)
mc.descriptor.internal_method()
mcc.descriptor.internal_method()
