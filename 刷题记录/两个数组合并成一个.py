def merge_sort(a, b):
    ret = []
    while len(a)>0 and len(b)>0:
        if a[0] <= b[0]:
            ret.append(a[0])
            a.remove(a[0])
        if a[0] >= b[0]:
            ret.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        ret += b
    if len(b) == 0:
        ret += a
    return ret
# 以上remove 方法可能比较耗时，应采用以下 索引元素比较法替代头位元素比较法：
def merge_sort(a, b):
    ret = []
    i = j = 0
    while len(a) >= i + 1 and len(b) >= j + 1:
        if a[i] <= b[j]:
            ret.append(a[i])
            i += 1
        else:
            ret.append(b[j])
            j += 1
    if len(a) > i:
        ret += a[i:]
    if len(b) > j:
        ret += b[j:]
    return ret

if __name__ == '__main__':
    a = [1,3,4,6,7,78,97,190]
    b = [2,5,6,8,10,12,14,16,18]
    print(merge_sort(a, b))
