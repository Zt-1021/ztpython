# 题：网站要求用户输入用户名和密码进行注册。编写程序以检查用户输入的密码的有效性。
# 以下是检查密码的标准：
# 1. [a-z]之间至少有1个字母
# 2. [0-9]之间至少有1个数字
# 1. [A-Z]之间至少有一个字母
# 3. [$＃@]中至少有1个字符
# 4.最短交易密码长度：6
# 5.交易密码的最大长度：12
# 您的程序应接受一系列逗号分隔的密码，并将根据上述标准进行检查。将打印符合条件的密码，每个密码用逗号分隔。
# 例：如果以下密码作为程序的输入：
#
# ABd1234@1,a F1#,2w3E*,2We3345
# 然后，程序的输出应该是：
#
# ABd1234 @ 1


# pwds = input("请输入密码：")
# pwd = pwds.split(",")
# for j in pwd:
#     if 6 <= len(j) <= 12:
#         # 小写字母，数字，大写字母，其他符号
#         a = b = c = d = 0
#         for i in j:
#             if i.isdigit():
#                 b += 1
#             elif i.isalpha():
#                 if i.isupper():
#                     c += 1
#                 else:
#                     a += 1
#             elif i == '$' or i == '＃' or i == '@':
#                 d += 1
#         if a >= 1 and b >= 1 and c >= 1 and d >= 1:
#             print("密码具有有效性{}".format(j))
#         else:
#             print("密码不具有有效性{}".format(j))
#     else:
#         print("密码不具有有效性{}".format(j))


# import re
#
# pwds = input("请输入密码：")
# pwd = pwds.split(",")
# for i in pwd:
#     if re.search("[a-z]", pwd):
#         if re.search("[0-9]", pwd):
#             if re.search("[A-Z]", pwd):
#                 if re.search("[$#@]", pwd):
#                     print(i)
#


import re
value = []
print("请输入：")
items = [x for x in input().split(',')]
for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    else:
        pass
    if not re.search("[a-z]", p):
        continue
    elif not re.search("[0-9]", p):
        continue
    elif not re.search("[A-Z]", p):
        continue
    elif not re.search("[$#@]", p):
        continue
    elif re.search("\s", p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))
