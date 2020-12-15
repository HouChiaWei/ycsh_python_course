# 撰寫一程式，程式檔名為 is_prime.py
# 提示使用者輸入一數字（100 以內的正整數），判斷此數字是否為質數，
# 若為質數，顯示 '是質數' ，反之顯示 '不是質數' 。
x = int(input("請輸入一個100以內的數字："))
for i in range(2,x-1):
    if x % i == 0:
        print("不是質數")
        break
else:
    print("是質數")