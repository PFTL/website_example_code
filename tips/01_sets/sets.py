var1 = frozenset('mississipi')
var3 = set('amazon')

print(id(var1))

var1 |= var3
print(id(var1))