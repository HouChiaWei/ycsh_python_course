x = int(input("請輸入一個數字："))
for i in range(2,x-1):
    if x % i == 0:
        print("不是質數")
        break
else:
    print("是質數")