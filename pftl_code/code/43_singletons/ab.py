class MySingleton:
    pass


ms1 = MySingleton()
ms2 = MySingleton()
print(ms1 is ms2)