a = 0


class Animal:
    # 单例模式
    def __new__(cls, *args, **kwargs):
        if cls is None:
            cls = super(Animal).__new__()
        return cls

    def eat(self):
        print("吃")
        print("吃")
        print("吃")


class Cat(Animal):
    # def __init__(self, name, weight):
    #     self.name = name
    #     self.weight = weight

    # def __str__(self):
    #     return "zhe shi yi ge kong fang fa %s :%d" % (self.name, self.weight)
    pass


# cat = Cat()
# print(cat.eat())


def main():
    print("这是一个主方法")


if __name__ == "__main__":
    print("执行了主方法")
    main()

file = open("readme.txt")
text = file.read()
file.write("yuzh844e")
print(text)
file.close()
