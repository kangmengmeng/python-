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


#3、字符串替换
#a) replace()函数可以替换string中的单个字符，也可以替换连续的字符，但无法生成字符替换映射表
s='We Are Happy'
t=s.replace(' ','%20')
print(t)   # 将空格替换为%20，输出 We%20Are%20Happy

#PS:pandas 里面也有一个replace()函数，其用法更加多样化。比如，可以加入一个字典，用于替换对不同的值进行替换。
s = pd.Series([0, 1, 2, 3, 4])
s.replace({0:'a',1:'b'})
Out[2]: 
0    a
1    b
2    2
3    3
4    4

#b)使用translate()函数，需要使用str.maketrans('','',del) 生成一个表，其中第一个参数表示被替换的字符，第二个参数为替换的字符，第三个参数为要删除的字符
import string
s = 'We Are Happy'
remove = string.punctuation  # 返回所有的标点符号  string.ascii_lowercase返回小写字母；string.ascii_uppercase返回大写字母；
                                                 # ascii_letters返回大小写字母；string.digits 返回0-9数字
table = str.maketrans(' ','%','')   # 一个参数与第二个参数的长度必须相等
print(s.translate(table))

#c) re.sub(pattern, repl, string, count)
#   第一个参数为被替换的参数，第二个参数是替换后的字符串，第三个参数为输入的字符串，第四个参数指替换个数。默认为0，表示每个匹配项都替换。
import re 
s='We Are Happy'
t=re.sub(' ','%20',s)
print(t)


