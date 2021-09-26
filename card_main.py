# 由用户决定什么时候退出
import card_tools

while True:
    # 显示菜单功能
    card_tools.show_menu()
    action_str = input("请选择希望执行的操作")
    print("您选择的操作是：%s" % action_str)
    # 1,2,3针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            card_tools.new_card()
        # 显示全部
        elif action_str == "2":
            card_tools.show_all()
        # 查询名片
        elif action_str == "3":
            card_tools.search_card()
        pass
    elif action_str == "0":
        print("欢迎再次使用")
        # pass只是一个占位符，不会执行任何操作
        break
    else:
        print("您的输入不正确，请重新选择")

a = 1
b = 2
a, b = (b, a)
