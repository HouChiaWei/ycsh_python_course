#for i in range(1,10) :
    #for j in range(1,10) :
        #print(i,'*',j,'=',i*j,';')
#j=1
#i=1
#while i <10:
    #print(i,'*',j,'=',i*j,';')
   # j+=1
    #if j==10:
      #  j=1
       # i+=1

for i in range (1,10) :
    s = ' '
    for j in range (1,10) :
        s += str(i) + '*' + str(j) + '=' + str(i*j) + ';'
    print(s)