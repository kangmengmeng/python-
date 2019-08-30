#优化后代码
s=[1,2,2,1,3,1]
def tick(nums):
    l = len(nums)
    if l < 2:
        return l
    nums.sort()
    start = 0
    for x in range(1,l):
        if nums[start] != nums[x]:
            nums[start+1] = nums[x]
            start += 1
    return start+1

print(tick(s))
