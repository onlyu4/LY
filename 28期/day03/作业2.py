
#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                    O\ = /O
#                ____/`---'\____
#              .   ' \\| |// `.
#               / \\||| : |||// \
#             / _||||| -:- |||||- \
#               | | \\\ - /// | |
#             | \_| ''\---/'' | |
#              \ .-\__ `-` ___/-. /
#           ___`. .' /--.--\ `. . __
#        ."" '< `.___\_<|>_/___.' >'"".
#       | | : `- \`.;`\ _ /`;.`/ - ` : | |
#         \ \ `-. \_ __\ /__ _/ .-` / /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
#
# .............................................
#          佛祖保佑             永无BUG
#  佛曰:
#          写字楼里写字间，写字间里程序员；
#          程序人员写程序，又拿程序换酒钱。
#          酒醒只在网上坐，酒醉还来网下眠；
#          酒醉酒醒日复日，网上网下年复年。
#          但愿老死电脑间，不愿鞠躬老板前；
#          奔驰宝马贵者趣，公交自行程序员。
#          别人笑我忒疯癫，我笑自己命太贱；
#          不见满街漂亮妹，哪个归得程序员？

# HR⼈人⼒力力资源管理理.
# 1、菜单: ("查看员⼯工信息", "添加员⼯工信息", "修改员⼯工信息", "删除员⼯工信息", "退出")
# 2、添加员⼯工信息:
# ⽤用户输⼊入员⼯工的基本信息(id, name, birthday, salary, input_time), 将员⼯工信息写⼊入到⽂文件emp.db⽂文件内
# 3、修改员⼯工信息:
#   显示所有员⼯工信息.然后让⽤用户选择要修改的员⼯工的id.然后让⽤用户输⼊入员⼯工的⼯工资, 将员⼯工的⼯工资修改为⽤用户输⼊入的⼯工资.其余内容不不做改动
# 4、删除员⼯工信息: 显示所有员⼯工信息.然后⽤用户选择要删除的员⼯工id, 根据⽤用户输⼊入的id删除该员⼯工的全部信息
# 5、查看员⼯工信息:
#   显示出所有员⼯工的基本信息

import json
def menu():
    a = True
    while a:
        user_input = input("查看员工信息\t添加员工信息\n修改员工信息\n删除员工信息\n退出")
        if user_input == "查看员工信息":
            see()
        elif user_input == "添加员工信息":
            add()
        elif user_input == "修改员工信息":
            revise()
        elif user_input == "删除员工信息":
            del_info()
        elif user_input == "退出":
            a = False
        else:
            print("请输入正确的选项")
    pass

def add():
    dict_info ={}
    with open("emp.db","a",encoding="utf-8")as f:
        id = input("请输入员工的ID：")
        name = input("请输入员工的姓名：")
        birthday = input("请输入员工的生日：")
        salary = input("请输入员工的工资：")
        input_time = input("请输入员工的入职时间")
        dict_info["ID"] = id
        dict_info["name"] = name
        dict_info["Birthy"] = birthday
        dict_info["Salary"] = salary
        dict_info["Input_time"] = input_time
        print(dict_info)
        f.write(str(f"{dict_info}\n"))
        menu()


def del_info():
    with open("emp.db", "a", encoding="utf-8")as f:

    pass


def revise():
    pass


def see():
    pass
