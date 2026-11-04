total=0
count=0
for num in range ( 1,1000):
    if num %3 ==0 or num %5 ==0 :
        total= total+num
        count= count+1
print ( count , total)



work =input ('What do you want to do? (1,2)')


if work =='1':
    for w in  range ( 100):
        print (' hello')
        
        
elif work =='2':
    for w in  range ( 50):
        print (' hope')
        
else :
    print (' This character is wrong')
    


adad= int ( input ('  please enter the one character:'))
for i in range (1, adad+1):
    if adad % i==0:
        print(i)

    

        
           