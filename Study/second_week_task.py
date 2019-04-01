#1、有变量name = "aleX leNb" 完成如下操作：
#1)  移除 name 变量对应的值两边的空格,并输出处理结果
name = "aleX leNb"
print(name.strip())

#2)  移除name变量左边的"al"并输出处理结果
import re
print(name.replace("al",""))    #replace 替换字符串
print(name.strip("al"))

#移除name变量右面的"Nb",并输出处理结果
print(name.replace("Nb",""))
print(name.rstrip("Nb"))

#移除name变量开头的a"与最后的"b",并输出处理结果
print(name.strip("ab"))  #strip  去掉首尾的字符

#判断 name 变量是否以 "al" 开头,并输出结果
print(name.startswith("al"))

#判断name变量是否以"Nb"结尾,并输出结果
print(name.lstrip("Nb"))


#