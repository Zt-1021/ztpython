# 题：使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字。
# 提示：考虑使用yield。


def num(n):
    i = 0
    while i < n:
        j = i
        i += 1
        if j % 7 == 0:
            yield j


for i in num(100):
    print(i)
