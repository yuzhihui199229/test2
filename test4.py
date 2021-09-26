a = 0


class Animal:
    def eat(self):
        print("吃")


class Cat(Animal):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "zhe shi yi ge kong fang fa %s :%d" % (self.name, self.weight)


cat = Cat("xiao", 77)
print(cat.eat())
