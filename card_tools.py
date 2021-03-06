# 定义所有的名片的字典
card_list = []


def show_menu():
    print("欢迎使用：【名片管理系统】V:1.0")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("4.退出系统")


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    # 1.提示用户输入名片的详细信息
    name = input("请输入姓名：")
    phone = input("请输入电话")
    qq = input("请输入QQ")
    email = input("请输入邮箱")
    # 2.使用用户的信息建立一个名片字典
    card_dict = {
        "name": name,
        "phone": phone,
        "qq": qq,
        "email": email
    }
    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    # 4.提示用户添加成功
    print("添加名片成功%s" % name)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")
    # 判断是否存在名片记录
    if len(card_list) == 0:
        print("当前没有任何的名片记录，请使用新增功能添加名片！")
        # return可以返回一个函数的执行结果
        # 下方的代码不会被执行
        # 如果return 的后面没有任何的内容，表示会返回调用函数的位置
        return
    # 打印表头
    for name in ["姓名", "电话", "qq", "邮箱"]:
        print(name, end="\t\t")
    # 打印分割线
    print("=" * 50)
    # 遍历名片的列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名")
    # 2.便利名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t\t电话\t\t\tqq\t\t\t邮箱")
            print("=" * 50)
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
            # 针对找到名片记录执行修改的操作
            deal_card(card_dict)
            break
    else:
        print("抱歉没有找到")


def deal_card(find_dict):
    print(find_dict)
    action_str = input("请选择要执行的操作：1.修改 2.删除 0.返回上级菜单")
    if action_str == "":
        print("修改名片")
    elif action_str == "2":
        print("删除名片")
