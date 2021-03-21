def make_numbers(start, stop, step):
    i = start
    while i<=stop:
        yield i
        i += step


for i in make_numbers(1, 20, 2):
    print(i)