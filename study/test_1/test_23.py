# 题：定义一个类，它具有类参数并具有相同的实例参数。
# 提示：定义一个实例参数，需要在__init__方法中添加它。您可以使用构造参数初始化对象，也可以稍后设置该值


class Car:

    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

