# 题：编写一个接受句子并计算字母和数字的程序。假设为程序提供了以下输入：
# Hello world! 123
# 然后，输出应该是：
# 字母10
# 数字3


s = input("请输入：")
# 数字a;字母b
a = 0
b = 0
for i in s:
    if i.isdigit():
        a += 1
    elif i.isalpha():
        b += 1
print("字母{},数字{}".format(b, a))
print("数字%d,字母%d" % (a, b))

