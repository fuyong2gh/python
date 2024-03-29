card_list = []
def show_menu():
    """显示菜单"""
    print('*' * 50)
    print('欢迎使用【菜单管理系统】V1.0')
    print('')
    print('1. 新建名片')
    print('2. 显示全部')
    print('3. 查询名片')
    print('')
    print('0. 退出系统')
    print('*' * 50)
def new_card():
    """新建名片"""
    print('-' *50)
    print('功能：新建名片')

    #1. 提示用户输入名片信息
    name = input("请输入姓名：")
    phone = input('请输入电话：')
    qq = input("请输入 QQ 号码：")
    email = input("请输入邮箱：")

    #2将用户信息保存在一个字典中
    card_dict = {'name':name,
                 'phone':phone,
                 'qq':qq,
                 'email':email}
    #3将用户字典加到名片列表
    card_list.append(card_dict)

    print(card_list)

    #提示添加成功
    print('添加成功 %s 的名片' % card_dict['name'])
def show_all():
    '''显示全部'''
    print('-'*50)
    print('功能：显示全部')
    #1 判断是否为空表头
    if len(card_list)==0:
        print("提示: 没有任何名片记录!!!")
        return
    #打印表头
    for name in ['姓名','电话','QQ','邮箱']:
        print(name,end='\t\t')
    #打印分割线
    print('')
    print('='*50)

    for card_dict in card_list:
        print('%s\t\t%s\t\t%s\t\t%s' %(
            card_dict['name'],
            card_dict['phone'],
            card_dict['qq'],
            card_dict['email']))
def search_card():
    """搜索名片"""
    print('-'*50)
    print('功能：搜索名片')

    find_name = input("请输入要搜索的姓名")

    for card_dict in card_list:
        if card_dict['name'] == find_name:
            print('姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱')
            print('-'*40)
            print('%s\t\t\t%s\t\t\t%s\t\t\t%s' %(
                card_dict['name'],
                card_dict['phone'],
                card_dict['qq'],
                card_dict['email']
            ))
            deal_card(card_dict)
            break
    else:
        print('没有找到 %s' % find_name)
def deal_card(find_dict):

    print(find_dict)
    action = input("请选要执行的操作 【1】 修改 【2】 删除 【0】 返回上级")
    if action == '1':
        find_dict['name']=input_card_info(find_dict['name'],"姓名： ")
        find_dict['phone']=input_card_info(find_dict['phone'],"电话： ")
        find_dict['qq']=input_card_info(find_dict['qq'],"QQ: ")
        find_dict['email']=input_card_info(find_dict['email'],"邮箱: ")
        print('修改名片成功！ ')
    elif action == '2':
        card_list.remove(find_dict)
        print('删除名片成功！')
def input_card_info(dict_value,tip_message):
    result_str = input(tip_message)
    if len(result_str)>0:
        return  result_str
    else:
        return dict_value


