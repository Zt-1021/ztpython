# 问题：编写一个程序，接受一系列逗号分隔的4位二进制数作为输入，然后检查它们是否可被5整除。 可被5整除的数字将以逗号分隔的顺序打印。
# 例：
# 0100,0011,1010,1001
# 那么输出应该是：
# 1010

s = input("请输入：")
for i in s.split(','):
    j = int(i, 2)
    if j % 5 == 0:
        print(i)

