# coding:utf-8

none_list = [None, None, None]

print(none_list)
print(bool(none_list))
print(len(none_list))  # 打印长度
print([])
print(bool([]))

max_list = [1, "dewei", "xiaomu", 3.14, [1, 2, 3]]
print(max_list)
max_list2 = [1, 3.14]
print(max(max_list2))
print(min(max_list2))

id_address = id(max_list2)
print(id_address)  # 同一个内存编号
