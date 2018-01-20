class Person:
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print('Hello!',self.name)


p = Person('python')
p.say_hi()