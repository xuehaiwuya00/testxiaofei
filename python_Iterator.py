# 迭代器

# 这是一个列表（就是那个装球的箱子）
# my_list = [10, 20, 30, 40]
#
# # 从箱子伸进去一只手（获取迭代器）
# my_iterator = iter(my_list)  # iter() 就是"伸手"的动作
#
# # 用这只手一个一个往外掏
# print(next(my_iterator))  # 输出 10   （摸出第一个）
# print(next(my_iterator))  # 输出 20   （摸出第二个）
# print(next(my_iterator))  # 输出 30   （摸出第三个）
# print(next(my_iterator))  # 输出 40   （摸出第四个）

# 再摸第五个会怎样？
# print(next(my_iterator))  # 报错！StopIteration，意思是"箱子空了，没球了"

# my_list = [10, 20, 30, 40]
#
# # 你写的是这个：
# for item in my_list:
#     print(item)
#
# # Python 实际在背后干的是这个：
# my_iterator = iter(my_list)          # 1. 先伸手
# while True:
#     try:
#         item = next(my_iterator)     # 2. 不断取下一个
#         print(item)
#     except StopIteration:            # 3. 取完了就停止
#         break

# 场景：我想造一个"报数器"，从 1 报到 5，每次只报一个数。
# class Mycounter:
#     def __init__(self, max_num):
#         self.max = max_num
#         self.current = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.max:
#             raise StopIteration
#
#         result = self.current
#         self.current += 1
#         return result
#
# counter = Mycounter(5)

# 手动取
# print(next(counter))
# print(next(counter))
# # print(next(counter))
# # print(next(counter))
#
# # 自动取
# for num in counter:
#     print(num)

# 场景 1：读超大文件
# 普通写法（作死）：
# with open('超大文件.txt', 'r') as f:
#     all_lines = f.readlines()  # 把几百万行全读到内存，电脑卡死
#
# # 迭代器写法（正确）：
# with open('超大文件.txt', 'r') as f:
#     for line in f:  # f 本身就是迭代器，一行一行读
#         print(line)  # 每次只占用一行内存

# 手动实现迭代器
class Myiterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            curr_index = self.index
            self.index += 1
            return self.data[curr_index]
        else:
            raise StopIteration

my_iterator = Myiterator([1, 2, 3, 4])

for element in my_iterator:
    print(element)









