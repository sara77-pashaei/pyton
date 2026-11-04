import random
data=[]
count=0
for i in range(1000):
    rand=random.randint(1,6)
    data.append(rand)
    if rand==4:
        count+=1

print('the count of 4 is:',count)
per=count/1000
print('the probability  is:',per)
    
