class Person:
    __slots__ = 'age', 'name'
    def __init__(self, age, name):
        self.age = age
        self.name = name

class Student(Person):
    def __init__(self, age, name, course):
        super(Student, self).__init__(age, name)
        self.course = course

if __name__ == '__main__':
    me = Student(35, 'Aquiles', 'Physics')
    print(me.__dict__)
    me.new_var = 10
    print(me.__dict__)
    print(me.__slots__)


