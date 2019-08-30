import sys
line1 = sys.stdin.readline().strip()
a=list(map(int, line1.split()))
line2 = sys.stdin.readline().strip()
b=list(map(int, line2.split()))
ans=0
flag=0
c=0
min=sum(b)
for i in range(a[1]):
    ans+=b[i]
for i in range(a[0]-a[1]):
        if(ans<min):
            min=ans
            c=i+1
        ans = ans - b[i] + b[i + a[1]]

print(c)


