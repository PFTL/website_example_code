mis = "mississippi"
ama = "amazon"
var1 = set(mis)
var2 = set(ama)

letters = var1 | var2

for i in letters:
    print(i)