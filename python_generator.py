# 生成器

# 写法1：生成器函数（带 yield 关键字）

# 这是一个生成器函数（注意有 yield）
# def my_generator():
#     print("开始生产第1个馒头")
#     yield 1  # 生产第1个，给你，然后暂停
#     print("开始生产第2个馒头")
#     yield 2  # 生产第2个，给你，再暂停
#     print("开始生产第3个馒头")
#     yield 3  # 生产第3个，给你，结束
#
# # 调用函数不会立即执行，而是返回一个生成器对象
# gen = my_generator()
# print(gen)  # <generator object my_generator at 0x...>
#
# # 用 next() 拿下一个值
# print(next(gen))  # 打印：开始生产第1个馒头  然后打印：1
# print(next(gen))  # 打印：开始生产第2个馒头  然后打印：2
# print(next(gen))  # 打印：开始生产第3个馒头  然后打印：3
# 再 next(gen) 就会报 StopIteration 错误（因为没馒头了）

# 写法2：生成器表达式（像列表推导式，但用圆括号）

# 列表推导式（一次性生成所有数，占内存）
# list_nums = [x * 2 for x in range(5)]
# print(list_nums)  # [0, 2, 4, 6, 8]

# 生成器表达式（用圆括号，惰性生成）
# gen_nums = (x * 2 for x in range(5))
# print(gen_nums)  # <generator object <genexpr> at 0x...>

# # 一个个取
# print(next(gen_nums))  # 0
# print(next(gen_nums))  # 2
# print(next(gen_nums))  # 4
# # 还可以循环取
# for num in gen_nums:
#     print(num)  # 继续打印 6, 8

# 场景1：处理超大文件（比如10GB的日志）
# 错误做法：一次性读全部，内存直接爆掉
# with open('big_file.txt') as f:
#     lines = f.readlines()  # 10GB全读到内存，电脑卡死
#     for line in lines:
#         print(line)

# 正确做法：用生成器，一行一行读
# def read_big_file(file_path):
#     with open(file_path) as f:
#         for line in f:  # 文件对象本身就是一个生成器
#             yield line  # 每次只返回一行
#
# for line in read_big_file('big_file.txt'):
#     print(line)  # 内存里永远只有一行

# 场景2：生成无限序列（比如所有自然数）
# 列表没法表示无限序列，但生成器可以
# def all_numbers():
#     n = 0
#     while True:  # 无限循环
#         yield n
#         n += 1
#
# gen = all_numbers()
# print(next(gen))  # 0
# print(next(gen))  # 1
# print(next(gen))  # 2
# 你要多少取多少，不取它就不算，永远不会内存溢出

# 场景3：节省CPU和时间（只算你需要的）
# 普通做法：先算100万个数的平方，存起来
# squares = [i**2 for i in range(1000000)]  # 等很久，占很多内存
# 但其实你可能只需要前10个

# 生成器做法：现用现算
# squares_gen = (i**2 for i in range(1000000))
# for i in range(10):
#     print(next(squares_gen))  # 只算前10个，后面的根本不碰

# 手动实现生成器
def even_range(start, end):
    current = start
    while current < end:
        if current % 2 == 0:
            yield current
        current += 1

even_nums = even_range(0, 10)

print(next(even_nums))
print(next(even_nums))
print(next(even_nums))
print(next(even_nums))











