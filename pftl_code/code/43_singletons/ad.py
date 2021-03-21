class MyFile:
    file = []

    def __init__(self, filename):
        if len(self.file) == 0:
            self.file.append(open(filename, 'w'))

    def write(self, line):
        self.file[0].write(line + '\n')


f = MyFile('test.txt')

f.write('test1')
f.write('test2')

f2 = MyFile('test.txt')
f2.write('test3')
f2.write('test4')

print(f2 is f)