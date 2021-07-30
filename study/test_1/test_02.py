# 问题:编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8
# 则输出为:40320
'''

    def fn(i):
        s = 1
        while i>=1:
            s =s*i
            i-=1
        print(s)

    if __name__ == "__main__":
        fn(8)

'''


def fact(i):
    if i == 0:
        return 1
    return i*fact(i-1)


x = int(input('请输入一个数字：'))
print(fact(x))


