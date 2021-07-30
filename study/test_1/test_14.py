# 题：编写一个接受句子的程序，并计算大写字母和小写字母的数量。
# 假设为程序提供了以下输入：
# Hello world!
# 然后，输出应该是：
# 大写实例 1
# 小写实例 9


# 大写a,小写b
a = 0
b = 0
s = input("请输入:")
for i in s:
    if i.islower():
        b += 1
    elif i.isupper():
        a += 1
print("大写实例{},小写实例{}".format(a, b))
