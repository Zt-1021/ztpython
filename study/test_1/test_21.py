# 机器人从原点（0,0）开始在平面中移动。 机器人可以通过给定的步骤向上，向下，向左和向右移动。 机器人运动的痕迹如下所示：
# UP 5
# DOWN 3
# LETF 3
# RIGHT 2
# 方向之后的数字是步骤。 请编写一个程序来计算一系列运动和原点之后距当前位置的距离。如果距离是浮点数，则只打印最接近的整数。
# 例：如果给出以下元组作为程序的输入：
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# (UP 5,DOWN 3,LEFT 3,RIGHT 2)
# 然后，程序的输出应该是：2

import math
x = y = 0
operation = input("请输入")
for i in operation.split(","):
    j = i.split(" ")
    if j[0] == "UP":
        x += int(j[1])
    elif j[0] == "DOWN":
        x -= int(j[1])
    elif j[0] == "LEFT":
        y += int(j[1])
    elif j[0] == "RIGHT":
        y -= int(j[1])

k = math.sqrt(x**2 + y**2)
print(int(k))
