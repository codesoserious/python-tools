# -*- coding: utf-8 -*-

"""
@author: Andrew
@software: PyCharm
@file: table.py
@time: 2021/11/20 9:25 
"""
import requests
from prettytable import prettytable as tables


def loop_method():
    loop_control = True
    token = ''
    while loop_control:
        if len(token) == 0:
            print("===================请输入Code-Hub 个人token=========")
            token = input("input token:")
            continue
        else:
            print(f"Info:您的个人token: {token}")
            print("==========================请输入项目id,注意是纯数字==============")
            projectID = input('input 项目ID:')
            print("Info: 你输入的项目ID是" + projectID)
            # isinstance(projectID, str) and
            try:
                int_product = int(projectID)
            except BaseException as exe:
                print(f"Error: 抱歉:您的项目Id:{projectID}不是纯数字,请从新输入")
                continue
            if len(projectID) > 0 and type(int(int_product)) == int:
                table = tables.PrettyTable()
                tableBody = [['121212', 'https://www.baidu.com', '12121212'],
                             ['121212', 'https://www.baidu.com', '12121212']]
                # 定义表头
                table.field_names = ["name", "age", "sex"]
                # 增加一行数据，列表里的元素按照顺序对应表头
                print(" ")
                print("==============================MR合入请求信息=============================")
                for body in tableBody:
                    table.add_row(body)
                    # print(type(body))
                print(table)
                print(" ")
                print(" ")
                print("=============退出则直接关闭doc窗口,否则继续回车输入项目Id=================")
            else:
                # resp = requests.get('https://www.baidu.com')
                # if resp.status_code != 200:
                #     pass
                # elif resp.status_code == 404:
                #     print("网页地址找不到")
                # else:
                #     print(type(resp.status_code))
                #     print(f"百度请求状态码:{resp.status_code}%s", resp.status_code)
                print('=====================请输入有效的项目id============')


if __name__ == "__main__":
    loop_method()
    # loop_control = True
    # token = ''
    # while loop_control:
    #     if len(token) == 0:
    #         print("========请输入Code-Hub 个人token=========")
    #         token = input("inout token:")
    #         continue
    #     else:
    #         print(f"token:{token}")
    #         print("=====按回车键并输入项目id,注意是纯数字")
    #         projectID = input('项目ID:')
    #         print("-------" + projectID)
    #         if isinstance(projectID, str) and len(projectID) > 0 and type(int(projectID)) == int:
    #             table = tables.PrettyTable()
    #             tableBody = [["Jruing", "23", "男"], ["Jruing", "23", "男"]]
    #             dicts = {"type": 12343}
    #             # 定义表头
    #             table.field_names = ["name", "age", "sex"]
    #             # 增加一行数据，列表里的元素按照顺序对应表头
    #             print("                                           ")
    #             print("===============MR合入请求信息======================")
    #             for body in tableBody:
    #                 table.add_row(['121212','https://www.baidu.com','12121212'])
    #                 print(type(body))
    #             print(table)
    #             print("=============退出则直接关闭doc窗口,否则继续回车输入项目Id=================")
    #         else:
    #             resp = requests.get('https://www.baidu.com')
    #             if resp.status_code != 200:
    #                 pass
    #             elif resp.status_code == 404:
    #                 print("网页地址找不到")
    #             else:
    #                 print(type(resp.status_code))
    #                 print(f"百度请求状态码:{resp.status_code}%s", resp.status_code)
    #                 print('=========请输入有效的项目id============')
