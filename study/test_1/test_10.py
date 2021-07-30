# 问题:编写一个程序，接受一系列空格分隔的单词作为输入，并在删除所有重复的单词并按字母数字排序后打印这些单词。
# 假设向程序提供以下输入:
# hello world and practice makes perfect and hello world again
# 则输出为:
# again and hello makes perfect practice world


str01 = input("请输入一段字符：")
list01 = str01.split(' ')
str02 = set(list01)
list02 = list(str02)
list02.sort()
print(list02)


# x = [4,  6,  2,  1,  7,  9]
# print(x.sort())


# x = [4,  6,  2,  1,  7,  9]
# x.sort()
# print(x)

# x = [4,  6,  2,  1,  7,  9]

# print(sorted(x))
