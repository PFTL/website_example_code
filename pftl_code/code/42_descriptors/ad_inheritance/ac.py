class MyList(list):
    pass


var = MyList([1, 2, 3])
print(len(var))

var.my_info = 'This is my info'


setattr(var, 'my_info', 'Updated Info')
d = getattr(var, 'my_info')
print(d)
