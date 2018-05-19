#!/usr/bin/env python
"""
该模块用来定义系统的菜单模板
"""
# 主程序中的主菜单

index_default_menu = '''
-------------------------------------------------------------------------
                             模拟程序

{0}                                  今天 {1}     星期{2}
-------------------------------------------------------------------------
【1】登录系统......【2】后台管理...... 【3】退出系统......
'''
#【4】...... 【5】......

# 主程序中的用户登录后的显示菜单

index_logined_menu = '''
-------------------------------------------------------------------------
                             模拟程序

\033[1;32m{0}\033[0m                   今天 {1}   星期{2}
-------------------------------------------------------------------------
【1】用户中心......【2】后台管理...... 【3】退出系统...... 
'''

# 主程序中的用户中心菜单

index_user_center = '''
-------------------------------------------------------------------------
                                用户中心

当前用户:{0}                              今天 {1}   星期{2}
-------------------------------------------------------------------------
【1】修改密码....... 【2】修改资料....... 【3】注销........ 【4】返回........

'''

# # 用户中心按键对应功能模块 clsUsers
# user_center_func = {
#     "1": {"module": "modules.users", "func": "modify_password"},
#     "2": {"module": "modules.users", "func": "modify_user_info"},
#     "3": {"module": "modules.report", "func": "print_bill_history"},
#     "4": {"module": "modules.report", "func": "print_shopping_history"},
#     "5": {"module": "modules.users", "func": "logout"}
# }

'''
# 用户中心按键对应功能模块 clsUsers
通过字典定义
'''
# user_center_func = {
#     "1": {"module": "modules.clsUsers", "func": "modify_password"},
#     "2": {"module": "modules.clsUsers", "func": "modify_user_info"},
#     "3": {"module": "modules.clsReport", "func": "print_bill_history"},
#     "4": {"module": "modules.clsReport", "func": "print_shopping_history"},
#     "5": {"module": "modules.clsUsers", "func": "logout"}
# }




# 后台管理模板
index_admin = '''
------------------------------------------------------------------------------
                               后台管理

用户:{username}
------------------------------------------------------------------------------
【1】创建用户     【2】删除用户         【3】解锁用户    【4】退出后台管理
   
'''


# 显示用户基本信息模板
user_info = '''
------------------------------------------------------------------------------
                               用户基本信息

用 户 名:{username}        姓    名:{name}               手    机:{mobile}
用户权限:{role}            是否锁定:{islocked}           是否删除:{isdel}
------------------------------------------------------------------------------
'''


