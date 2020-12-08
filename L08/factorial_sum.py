sum=1
n=int(input())
x=1

for i in range(1,n+1):
    x*=i
    sum+=x

print(sum)
