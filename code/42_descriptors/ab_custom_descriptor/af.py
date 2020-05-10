class MyDescriptor:
    def __init__(self, val):
        self.val = val

    def __call__(self):
        print(self.val)


my_descriptor = MyDescriptor(1)
my_descriptor()