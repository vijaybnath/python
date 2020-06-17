# class and objects
class Robot:
    def __init__(self, Name, Color, Weight):
        self.name = Name
        self.color = Color
        self.weight = Weight

    def introduce_self(self):
        print("My name is " + self.name) # this in java

r1 = Robot("tom", "red", 30)
r2 = Robot("jerry", "blue", 40)


r1.introduce_self()
r2.introduce_self()

class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", False)

# p1 owns r2
p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()