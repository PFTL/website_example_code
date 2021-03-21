class Person:
    __slots__ = 'age', 'name'
    def __init__(self, age, name):
        self.age = age
        self.name = name

class Student(Person):
    __slots__ = 'course'
    def __init__(self, age, name, course):
        super(Student, self).__init__(age, name)
        self.course = course


if __name__ == '__main__':
    me = Student(35, 'Aquiles', 'Physics')
    print(me.__slots__)
    me.new_var = 10



