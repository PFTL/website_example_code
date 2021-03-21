class MySingleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        print('new')
        if not isinstance(cls.instance, cls):
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance


class NewSingleton(MySingleton):
    def __str__(self):
        return 'This is a new singleton'


ms1 = MySingleton()
ms2 = NewSingleton()
print(ms1 is ms2)
print(ms2)
print(ms1.instance)
print(ms2.instance)