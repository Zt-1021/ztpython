# 问题:编写一个程序，接受一行序列作为输入，并在将句子中的所有字符大写后打印行。
# 假设向程序提供以下输入:
# Hello world
# Practice makes perfect
# 则输出为:
# HELLO WORLD
# PRACTICE MAKES PERFECT


def f(a):
    i = a.upper()
    return i


if __name__ == "__main__":
    print(f('Hello world'))
    print(f('Practice makes perfect'))


# str = input("请输入一段字符：")
# if str:
#     s = str.upper()
# print(s)
