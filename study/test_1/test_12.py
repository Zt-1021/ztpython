# 题：编写一个程序，它将找到1000到3000之间的所有这些数字（均包括在内），这样数字的每个数字都是偶数。
# 获得的数字应以逗号分隔的顺序打印在一行上。

values = []
for i in range(1000, 3001):
    s = str(i)
    if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0:
        values.append(i)
print(values)
