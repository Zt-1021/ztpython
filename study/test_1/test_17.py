# 题：编写一个程序，根据控制台输入的事务日志计算银行帐户的净金额。 事务日志格式如下所示：
# D 100
# W 200
#
# D表示存款，而W表示提款。
# 假设为程序提供了以下输入：
# D 300
# D 300
# W 200
# D 100
# 然后，输出应该是：
# 500


# money = 0
# i = 0
# s = input("请输入")
# while i < 5:
#     L = s.split(' ')
#     if L[1] == "D":
#         money += L[2]
#     elif L[1] == "W":
#         money -= L[2]
#     else:
#         print("请输入正确的格式")
#     i += 1
# print(money)


netAmount = 0
while True:
    print("请输入：")
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation == "D":
        netAmount += amount
    elif operation == "W":
        netAmount -= amount
    else:
        pass
print(netAmount)

