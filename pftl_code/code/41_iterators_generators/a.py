def make_numbers():
    print('Making a number')
    yield 1
    print('Making a new number')
    yield 2
    print('Making the last number')
    yield 3

a = make_numbers()
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

b = make_numbers()

for i in b:
    print(i)