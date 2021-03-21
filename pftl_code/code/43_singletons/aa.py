class MySingleton:
    print('My Singleton!')
    instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.instance, cls):
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance


ms1 = MySingleton()
ms2 = MySingleton()
print(ms1 is ms2)