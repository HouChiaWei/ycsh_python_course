a = int(input("請輸入一個數字："))
b = int(input("請輸入一個數字："))
for i in range(a,b+1):
    for x in range(2,i):
        if i % x == 0:
            i+=1
            break
    else:
        print(i)