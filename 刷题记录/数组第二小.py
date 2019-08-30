def seconde_min(lt):
    d={}         #设定一个空字典
    for i, v in enumerate(lt):#利用函数enumerate列出lt的每个元素下标i和元素v
        d[v]=i   #把v作为字典的键，v对应的值是i
    lt.sort()    #运用sort函数对lt元素排
    y=lt[1]      #此时lt中第二小的下标是1，求出对应的元素就是字典对应的键
    return d[y]  #根据键找到对应值就是所找的下标
lt = [1, 3, 5, 7, 2, 4, 6]
print(seconde_min(lt))
