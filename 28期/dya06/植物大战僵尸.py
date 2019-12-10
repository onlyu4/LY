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

class Jiamgshi:
    def __init__(self,name,life,attack):
        self.name = name
        self.life = life
        self.attack = attack

    def chi(self,zw):
        zw.life -= self.attack


class Zhiwu:
    def __init__(self,name,life,attack):
        self.name = name
        self.life = life
        self.accack = attack

    def da(self,js):
        print(f"{self.name}在打{js.name}")
        js.life -= self.accack
        print(f"{js.name}还有{js.life}滴血")


js1 = Jiamgshi("js1",1000,200)
zw1 = Zhiwu("zw1",2000,500)

if __name__ == '__main__':
    zw1.da(js1)
