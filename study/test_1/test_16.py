# 题：使用列表推导来对列表中的每个奇数。 该列表由一系列逗号分隔的数字输入。
# 假设为程序提供了以下输入：
# 1,2,3,4,5,6,7,8,9
# 然后，输出应该是：
# 1,3,5,7,9

values = input("请输入:")
numbers = [x for x in values.split(',') if int(x) % 2 != 0]
print(",".join(numbers))
