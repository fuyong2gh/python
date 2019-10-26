#!/usr/bin/python3
import cards_tools
while True:
    # TODO 显示菜单
    cards_tools.show_menu()
    action = input('请选择执行的操作:  ')

    print('您选择的操作是：%s' % action)

    #根据用户输入决定后续操作
    if action in ['1','2','3']:
            # 新增名片
        if action == '1':
            cards_tools.new_card()
        # 显示全部
        elif action == '2':
            cards_tools.show_all()
        # 查询名片
        elif action == '3':
            cards_tools.search_card()
    elif action == '0':
        print('欢迎再次使用！【名片管理系统】')
        break
    else:
        print('输入错误，请重新输入')
