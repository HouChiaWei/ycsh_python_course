h=float(input("請輸入身高："))
w=float(input("請輸入體重："))

h=h/100

bmi=w/h**2

bmi=round(bmi,2)

print("身高：",h,"m")
print("體重：",w,"kg")
print("BMI為：",bmi)

