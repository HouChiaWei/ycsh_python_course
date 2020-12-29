a = []
for i in range(5):
    i=int(input('請輸入第'+str(i+1)+'個數字：'))
    a.append(i)
a.sort()
a.reverse()
print(a)