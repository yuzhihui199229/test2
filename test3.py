def test(num):
    print("在函数内部的%d对应的地址是%d" % (num, id(num)))
    # 定义一个字符串变量
    result = "hello"
    print("函数要返回数据的内存地址是：%d" % id(result))
    return result


# 定义一个数字的变量
a = 10
print("a变量保存的地址是%d" % id(a))
# 调用test
r = test(a)
print("")
