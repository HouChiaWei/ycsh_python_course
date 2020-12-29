F = [0,1]
a = int(input('請輸入一個數字：'))
m = int(input('請輸入一個數字：'))
for n in range(2,m+1):
    Fn = F[n-1] + F[n-2]
    F.append(Fn)
for  i in range(a):
    F.remove(F[0])
print(F)