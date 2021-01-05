a = int(input("請輸入月份："))

if a >= 3 and a <= 5:
    print("春天")
elif a >= 6 and a <= 8:
    print("夏天")
elif a >= 9 and a <= 11:
    print("秋天")
elif a ==12 or a == 1 or a == 2 :
    print("冬天")
else:
    print("輸入錯誤")