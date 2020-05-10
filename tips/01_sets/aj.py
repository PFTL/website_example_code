var1 = frozenset('mississipi')
print(id(var1))
var2 = var1
print(id(var2))
var3 = set('amazon')

print(var2)

var1 |= var3
print(id(var1))

print(var2)