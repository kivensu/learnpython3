import pizza
# 导入整个模块
pizza.make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')

# 导入特定的函数
from pizza import make_pizza
make_pizza(20, 'tuna fish', 'mushrooms', 'potato', 'tomato')

# 使用as给模块指定别名
from pizza import make_pizza as mp
mp(25, 'tuna fish', 'potato', 'tomato')

# 导入模块中的所有函数
from pizza import *
make_pizza(25, 'tuna fish', 'tomato', 'cheese')

# 函数编写小指南
# 函数名要命名规范
# 函数应包含注解 文档字符串
# 给形参制定默认值时俩边不要留空格 关键字参数也一样
# 一行代码别超过79字符
# 程序包含多个函数的时候俩个空行将函数隔开
# 所有的import都应该放在开头
