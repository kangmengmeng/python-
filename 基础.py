# 1、大小写转换：
str = "www.runoob.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 

# 2、统计多维数组的行数和列数
# a）len  可以为list形式
A = [[1,2,8,9],[2,4,9,12]]
print len(A)    # 2  统计行数
print len(A[0]) # 4  统计列数
# 同样的如果是多维，每一维长度应该是 len(A[i])

# b) size  转成numpy数组形式
import numpy as np
A = [[1,2,8,9],[2,4,9,12]]
A=np.array(A)
number=A.size  # 计算 A 中所有元素的个数
col_number=np.size(A,0)  # 2  统计行数
row_number=np.size(A,1)  # 2  统计列数

# c) shape  必须转为numpy数组形式
A_dim=A.shape  # 以元组形式，返回数组的维数 (2,4)
print("X_dim:",X_dim)
print(A.shape[0])  # 统计行数 
print(A.shape[1])  # 统计列数


#3、
