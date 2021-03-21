class Person:
    def __init__(self, name, last_name):
        self.first_name = name
        self.last_name = last_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name


class Student(Person):
    def __init__(self, name, last_name, course):
        super().__init__(name, last_name)
        self.course = course

    def get_course_and_name(self):
        return self.course + '--' + self.get_full_name()

    def get_full_name(self):
        return self.first_name.capitalize() + ' ' + self.last_name.capitalize()


me = Person('aquiles', 'carattino')
print(me.first_name)
print(me.last_name)
print(me.get_full_name())
you = Student('matthijs', 'geerlings', 'Applied Physics')
print(you.first_name)
print(you.last_name)
print(you.get_full_name())
print(you.get_course_and_name())