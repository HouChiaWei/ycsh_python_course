sum=1
n=int(input())
x=1
i=1

while i < n+1:    #用while替換for迴圈
    x*=i
    sum+=x
    i+=1

print(sum)
