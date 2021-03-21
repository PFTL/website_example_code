class MyFile:
    _instance = None
    file = None

    def __init__(self, filename):
        if self.file is None:
            self.file = open(filename, 'w')

    def write(self, line):
        self.file.write(line + '\n')

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)

        return cls._instance


f = MyFile('test.txt')
f.write('test1')
f.write('test2')

f2 = MyFile('test2.txt')
f2.write('test3')
f2.write('test4')

print(f2 is f)