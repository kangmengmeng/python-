from collections import defaultdict
import sys
# n =7
# l = [1,2,1,3,4]

l = eval(input())
lst = list(map(int, input().split()))

if l <= 1:
    print(l)
else:
    data = [1]*l
    for i in range(1, l):
        for j in range(i):
            if lst[i] > lst[j]:
                data[i] = max(data[i], data[j] + 1)
    print(max(data))
