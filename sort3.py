a = []
for i in range(3):
    i=int(input('請輸入第'+str(i+1)+'個數字：'))
    a.append(i)
a.sort()
a.reverse()

for x in range(0,3):
    print(a[x])
