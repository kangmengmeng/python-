#求两个数的最大公约数   （辗转相除法）
def gcd(a,b):
    while b!=0:
        tmp=a%b   # 若a<b，则交换a,b
        a=b
        b=tmp
    return a
a=int(input())  # 输入一个数str类型，转为int型
b=int(input())
print(gcd(a,b))

       
