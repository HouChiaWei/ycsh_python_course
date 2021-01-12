scores = [['John',97],['Jack',83],['Jason',80],['Jimmy',77]]

x = input('請輸入姓名:')

#y = scores[scores.index(x)]

#print(scores[y][1])

for i in range(0,4):
    for j in range(0,2):
        y = scores[i][j].index(x)
        if y is True :
            print(scores[i][j])
            exit()
        j+=1
    i+=1

print('查無成績')

'未完成！！！！！！！！！！！！！！！！！！！！！！！！！'