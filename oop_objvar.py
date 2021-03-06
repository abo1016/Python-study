class Robot:
    '''表示一个带有名字的机器人'''
    population = 0

    def __init__(self,name):
        '''初始化'''
        self.name = name

        print("Initializing {}".format(self.name))

        Robot.population += 1
    def die(self):
        '''挂了'''
        print("{} is being destroyed".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There art still {:d} robots working".format(Robot.population))
    def say_hi(self):
        '''机器人的问候'''
        print("Greetings,my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        '''打印单前人口数量'''
        print("we have {:d} robots".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work .so let`s  destroy them.")
droid1.die()
droid2.die()

Robot.how_many()