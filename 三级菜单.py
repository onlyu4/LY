date = {
    '北京':{
        '昌平':{
            '沙河':['沙河地铁站','沙河高教园'],
            '昌平县城':['万科','乐多港']
        },
        '朝阳':{
            '望京':['浦项中心','绿地置业'],
            '望京西':['望承公园','望京西地铁站']
        },
    },
    '承德':{
        '双桥区':{
            '火神庙':['德汇大厦','承德商厦'],
            '头牌楼':['海棠花园','多多福网咖']
        },
        '双滦区':{
            '双塔山':['山塔山风景区','双塔山政府'],
            '三岔口':['枫林绿洲','泰丰时代城']
        }
    }
}
exit_1 = False
while not exit_1:
    for i in date:
        print(i)
    shuru = input('输入你要去的地点>>>>>>')
    if shuru in date:
        while not exit_1:
            for i2 in date[shuru]:
                print(i2)
            shuru2 = input('输入你要去的地点>>>>')
            if shuru2 == 'b':
                break
            elif shuru2 == 'q':
                exit_1 = True
            if shuru2 in date[shuru]:
                while not exit_1:
                    for i3 in date[shuru][shuru2]:
                        print(i3)
                    shuru3 = input('请输入你要去的地点>>>>')
                    if shuru3 == 'b':
                        break
                    elif shuru3 == 'q':
                        exit_1 = True
                    if shuru3 in date[shuru][shuru2]:
                        while not exit_1:
                            for i4 in date[shuru][shuru2][shuru3]:
                                 print(i4)
                            shuru4 = input('最后一层，按B返回')
                            if shuru4 == 'b':
                                break
                            elif shuru4 =='q':
                                exit_1 = True


